FROM python:3.11-alpine

WORKDIR /website

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

ENV FLASK_DEBUG=0

COPY requirements.txt requirements.txt

COPY schema.sql schema.sql

RUN apk add tk

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]
