FROM python:3.10-slim

WORKDIR /usr/src/app/

COPY ./ ./

RUN pip3 install .

RUN honeybot init

RUN honeybot run
