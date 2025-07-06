FROM python:3.11-slim

WORKDIR /app

# Copy requirements.txt first
COPY database/requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the database code
COPY database/ .

EXPOSE 5000

CMD ["python", "mysql.py"]
