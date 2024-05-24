FROM python:3.12.3-alpine3.20

WORKDIR /app

# Get the requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Bring in all the source code
COPY ./hello_world_site/ .

# Run the server and broadcast on port 8000
CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000" ]