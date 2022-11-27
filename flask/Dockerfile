FROM python:3.9.15-bullseye

WORKDIR /app

COPY ./app /app

RUN pip install -r requirements.txt


CMD ["uwsgi", "--ini", "/app/socialfish.ini"]