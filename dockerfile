FROM python:3.12-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["fastapi", "run", "main.py"]