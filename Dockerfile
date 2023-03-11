FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
