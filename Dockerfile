FROM ubuntu:jammy

ARG SERVER_FILES_URL
ARG SERVER_START_SCRIPT

# Core setup
RUN apt update
RUN apt -y install zip wget nano

RUN mkdir /yamcsr
WORKDIR /yamcsr

COPY entrypoints/run_server.sh .

RUN chmod +x run_server.sh

# MC server setup
RUN mkdir /yamcsr_server
WORKDIR /yamcsr_server

RUN apt -y install openjdk-17-jre

RUN wget $SERVER_FILES_URL -O server.zip
RUN unzip server.zip -d . && rm server.zip

RUN echo eula=true > eula.txt

RUN chmod +x $SERVER_START_SCRIPT

