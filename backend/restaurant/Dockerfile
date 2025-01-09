FROM python:3.11-slim

# Install pip if not already present
RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY ../shared /app/shared

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

