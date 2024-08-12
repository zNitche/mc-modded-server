FROM ubuntu:jammy

RUN mkdir /yamcsr_tasks
WORKDIR /yamcsr_tasks
COPY yamcsr_tasks/ .
COPY entrypoints/run_tasks.sh .

RUN apt update
RUN apt -y install nano cron python3 python3-pip
RUN pip3 install -r scripts/requirements.txt

RUN chmod +x run_tasks.sh
