# Use a slim version of Python 3.11
FROM python:3.11-slim
# Set the working directory inside the container
WORKDIR /app
# Copy only requirements first to leverage Docker cache
COPY backend/requirements.txt ./
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the backend code
COPY backend/ ./
# Copy frontend static and templates folders
COPY frontend/static ./static
COPY frontend/templates ./templates
# Expose the desired port
EXPOSE 8080
# Set environment variables (optional)
ENV NAME World
# Command to run the application
CMD ["python", "app.py"]
