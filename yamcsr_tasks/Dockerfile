FROM ubuntu:jammy

RUN mkdir /yamcsr_tasks
WORKDIR /yamcsr_tasks

COPY yamcsr_tasks/ .

RUN mkdir yamcsr_scripts
COPY yamcsr_scripts/ yamcsr_scripts

COPY entrypoints/run_tasks.sh .

RUN apt update
RUN apt -y install nano cron git python3 python3-pip
RUN pip install --upgrade pip

RUN pip3 install -r yamcsr_scripts/requirements.txt

RUN chmod +x run_tasks.sh
