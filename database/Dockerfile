# Use official Python image
FROM python:3.11-slim

WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set env for unbuffered logs
ENV PYTHONUNBUFFERED=1

# Entry point
CMD ["python", "mysql.py"]
