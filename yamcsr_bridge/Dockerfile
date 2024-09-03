FROM ubuntu:jammy

RUN mkdir /yamcsr_bridge
WORKDIR /yamcsr_bridge

COPY yamcsr_bridge/ .

RUN mkdir yamcsr_scripts
COPY yamcsr_scripts/ yamcsr_scripts

COPY entrypoints/run_bridge.sh .

RUN apt update
RUN apt -y install nano git python3 python3-pip
RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt
RUN pip3 install -r yamcsr_scripts/requirements.txt

RUN chmod +x run_bridge.sh
