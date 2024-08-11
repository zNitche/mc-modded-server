FROM ubuntu:jammy

RUN mkdir /cron
WORKDIR /cron
COPY cron/ .
COPY entrypoints/run_cron.sh .

RUN apt update
RUN apt -y install nano cron python3 python3-pip
RUN pip3 install -r scripts/requirements.txt

RUN chmod +x run_cron.sh
