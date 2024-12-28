# Base image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy the Django project to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Django collectstatic to generate static files
RUN python manage.py collectstatic --noinput
