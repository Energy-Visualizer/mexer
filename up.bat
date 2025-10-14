@echo off
setlocal enabledelayedexpansion

echo Building image...
docker build -t mexer . || exit /b 1

echo Creating Docker network...
docker network inspect mexerNetwork >nul 2>&1
if %ERRORLEVEL% neq 0 (
    docker network create mexerNetwork
)

echo Starting PostgreSQL Docker container...
docker rm -f postgres >nul 2>&1
docker run -d --name postgres -p 5432:5432 ^
  -e POSTGRES_USER=postgres ^
  -e POSTGRES_PASSWORD=postgres ^
  -v "%cd%\postgres\mexer_schema.sql:/docker-entrypoint-initdb.d/mexer_schema.sql" ^
  --network mexerNetwork ^
  postgres

echo Waiting for PostgreSQL to be ready...
:wait_pg
docker exec postgres pg_isready -U postgres >nul 2>&1
if %ERRORLEVEL% neq 0 (
    timeout /t 1 >nul
    goto wait_pg
)

echo Starting Mexer Docker container...
docker rm -f mexer >nul 2>&1
docker run --name mexer -dp 8000:8000 ^
  --env-file .env ^
  -v "%cd%\Mexer_site:/app:rw" ^
  --network mexerNetwork ^
  mexer python3 manage.py debug 0.0.0.0:8000

echo Running Migrations...
docker exec mexer python3 manage.py makemigrations
docker exec mexer python3 manage.py migrate

echo Inserting test data...
docker cp postgres/insert_test_data.sql postgres:/tmp/insert_test_data.sql
docker exec postgres psql postgresql://postgres:postgres@localhost -f /tmp/insert_test_data.sql

echo Creating superuser...
docker exec -it mexer bash -c "python3 manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL"

endlocal
