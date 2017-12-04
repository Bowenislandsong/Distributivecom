#FROM python:3
FROM ubuntu:latest

# Install.
RUN \
  apt-get -y update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget && \
  apt-get install -y python3 python && \
  apt-get install -y python3-pip && \
  apt-get install -y python-setuptools python-dev && \
  apt-get install -y python-pip && \
  pip install --upgrade pip

# Set environment variables.
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /client_share

ADD . /client_share

ADD ml.py /

CMD ["python3","ml.py"]
