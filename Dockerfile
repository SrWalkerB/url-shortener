FROM python:3.12-slim

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8080

EXPOSE 8080

CMD exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}
