FROM y12docker/bitcoind:0.10.0

RUN apt-get install -yq libdb5.1++

ADD bitcoin.conf /btc/bitcoin.conf

RUN mkdir -p /btc/data \
    && echo "alias rt='bitcoin-cli -conf=/btc/bitcoin.conf -regtest'" >> ~/.bashrc

ADD run /etc/service/bitcoind/
RUN chmod +x /etc/service/bitcoind/run

ADD bin/bitcoind bin/bitcoin-cli bin/bitcoin-tx /usr/bin/

EXPOSE 12333 12332
CMD ["/sbin/my_init"]
