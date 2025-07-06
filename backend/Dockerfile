# Use a slim version of Python 3.11
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY backend/requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend application code
COPY backend/ ./

# Copy frontend static and template files (if needed for rendering)
COPY frontend/static ./static
COPY frontend/templates ./templates

# Expose the application port
EXPOSE 8080

# Set environment variables (recommended syntax)
ENV NAME=World

# Start the Python application
CMD ["python", "app.py"]
