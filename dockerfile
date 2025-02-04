FROM python:3.12-slim-bookworm

WORKDIR /app

# Get the requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Bring in all the source code
# TODO: is the the best way to get the pgpass permissions to work
# The --chmod=0600 sets read/write permissions for the owner only
COPY --chmod=0600 ./Mexer_site/ .


# Set environment variables
# PGSERVICEFILE specifies the location of the PostgreSQL service file.
ENV PGSERVICEFILE=/app/.pg_service.conf
# PGPASSFILE specifies the location of the PostgreSQL password file.
ENV PGPASSFILE=/app/.pgpass

# Set up database connections
# Uncomment these to run migrations during the building process
# python3 manage.py makemigrations
# python3 manage.py migrate

# Run the server and broadcast on port 8000
CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000" ]

