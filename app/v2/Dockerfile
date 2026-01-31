# IoT Application v2 - Dockerfile
# Use Python slim image for smaller size
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (Docker layer caching optimization)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port 8888 (application port)
EXPOSE 8888

# Run the Flask application
CMD ["python", "app.py"]
