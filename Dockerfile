FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project  
COPY . .

# Run the application
CMD ["gunicorn", "schoolproject.wsgi:application", "--bind", "0.0.0.0:8000"]