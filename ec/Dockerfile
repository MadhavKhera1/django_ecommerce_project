# Base image with Python version
FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies using virtual environment
RUN python3 -m venv venv && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt && \
    /app/venv/bin/pip install --no-cache-dir django

# Copy project files
COPY . .

# Activate virtual environment and run Django command
CMD ["/bin/sh", "-c", ". venv/bin/activate && python manage.py runserver 0.0.0.0:8000"]

