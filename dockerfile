FROM python:3.12-slim-bookworm

WORKDIR /app

# Get the requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Bring in all the source code
COPY --chmod=0600 Mexer_site/ .
