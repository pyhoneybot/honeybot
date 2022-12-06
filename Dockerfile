# Version: 6.0.2
FROM ubuntu:latest
MAINTAINER John Doe "jdoe@example.com"
WORKDIR /usr/src/app/
COPY ./ ./
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
 && apt-get clean all
RUN pip3 install .
RUN honeybot init
