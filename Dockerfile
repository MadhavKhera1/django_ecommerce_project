# Base image with Python version
FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies using virtual environment
RUN python3 -m venv venv && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run command within virtual environment
CMD ["/app/venv/bin/python", "/app/manage.py", "runserver", "0.0.0.0:8000"]
