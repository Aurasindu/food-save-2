# Gunakan Python sebagai base image
FROM python:3.11

# Copy semua file ke dalam container
WORKDIR /app
COPY . /app

# Install dependency
RUN pip install -r requirements.txt

# Jalankan aplikasi
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]