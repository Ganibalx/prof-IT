FROM python:3.10-slim

WORKDIR /app

COPY ./code /app 

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip \
    && mkdir download

