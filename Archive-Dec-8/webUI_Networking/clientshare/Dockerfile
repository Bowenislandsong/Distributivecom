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
  apt-get install -y openjdk-8-jdk &&\
  pip install --upgrade pip

# Set environment variables.
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
#ENV PATH=$PATH:/usr/lib/jvm/java-8-openjdk/bin
#ADD . /clientshare
WORKDIR /clientshare

CMD ["bash"]
#CMD ["ls"]
#CMD ["cat","wsclient.py"]
CMD ["/usr/bin/java","-jar", "ModelTraining.jar"]
