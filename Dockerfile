FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DEBUG_MODE=False

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
