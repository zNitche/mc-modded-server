FROM ubuntu:jammy

ARG MODPACK_URL
ARG SERVER_START_SCRIPT

RUN mkdir /mc_server
WORKDIR /mc_server

RUN apt update
RUN apt -y install zip wget nano openjdk-17-jre

RUN wget $MODPACK_URL -O server.zip

RUN unzip server.zip -d . && rm server.zip

RUN echo eula=true > eula.txt
RUN chmod +x $SERVER_START_SCRIPT

