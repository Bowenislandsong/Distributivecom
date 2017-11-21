#
# Ubuntu Dockerfile
#
# https://github.com/dockerfile/ubuntu
#

# Pull base image.
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
  pip install --upgrade pip && \
  pip install cryptography && \
  pip install fernet && \ 
  pip install flask && \
  pip3 install flask && \
  pip3 install cryptography
#pip install flask && \
# Add files.
ADD . /root
# Set environment variables.
ENV HOME /root
ENV FLASK_APP client.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
# Define working directory.
WORKDIR /root

#PORTS
EXPOSE 5000
EXPOSE 9999
# Define default command.
CMD ["bash"]
#CMD ["export FLASK_APP=client.py"]
CMD ["python3" ,"-m", "flask" ,"run"]
#CMD ["python3","client.py"]


