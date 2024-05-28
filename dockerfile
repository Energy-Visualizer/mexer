FROM python:3.12.3-alpine3.20

WORKDIR /app

# Get the requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Bring in all the source code
COPY ./eviz_site/ .

# Set environment variables
ENV PGSERVICEFILE=/app/.pg_service.conf
ENV PGPASSFILE=/app/.pgpass

# Set up database connections
# python3 manage.py makemigrations
# python3 manage.py migrate

# Run the server and broadcast on port 8000
CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000" ]