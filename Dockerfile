FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Use gunicorn in production; bind to 8088
CMD ["gunicorn", "--bind", "0.0.0.0:8088", "app:app", "--workers", "2"]
