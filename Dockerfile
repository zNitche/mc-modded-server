FROM ubuntu:jammy

ARG MODPACK_URL
ARG SERVER_START_SCRIPT

# Core setup
RUN apt update
RUN apt -y install zip wget nano

RUN mkdir /mcmsr
WORKDIR /mcmsr

COPY entrypoints/run_server.sh .

RUN chmod +x run_server.sh

# MC server setup
RUN mkdir /mcmsr_server
WORKDIR /mcmsr_server

RUN apt -y install openjdk-17-jre

RUN wget $MODPACK_URL -O server.zip
RUN unzip server.zip -d . && rm server.zip

RUN echo eula=true > eula.txt

RUN chmod +x $SERVER_START_SCRIPT

