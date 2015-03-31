FROM gliderlabs/alpine:3.1
RUN apk-install python py-pip curl wget bash

WORKDIR /app

RUN apk-install git py-yaml
RUN git clone https://github.com/y12studio/pycoin
ADD pycoin.yml /app/
ADD patch.py /app/
RUN python patch.py
RUN cd pycoin && python setup.py install
