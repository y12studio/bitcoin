FROM y12docker/bitcoind:0.10.0

RUN apt-get install -yq libdb5.1++

ADD bitcoin.conf /btc/bitcoin.conf

RUN mkdir -p /btc/data \
    && echo "alias rt='bitcoin-cli -conf=/btc/bitcoin.conf -regtest'" >> ~/.bashrc

ADD run /etc/service/bitcoind/
RUN chmod +x /etc/service/bitcoind/run

WORKDIR /patcd

ADD bin/bitcoind bin/bitcoin-cli bin/bitcoin-tx /usr/bin/

ADD pycoin.conf /patcd/

RUN git clone https://github.com/y12studio/pycoin &&\
    cat pycoin.conf | sed '/^\#/d' | xargs -i sed -i 's|{}|' pycoin/pycoin/networks.py &&\
    cd pycoin && python setup.py install

EXPOSE 12333 12332
CMD ["/sbin/my_init"]
