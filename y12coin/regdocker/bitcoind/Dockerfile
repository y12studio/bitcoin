FROM y12docker/pbase:15.03

RUN apt-get -y update
RUN apt-get install -y python-software-properties

RUN add-apt-repository ppa:bitcoin/bitcoin
RUN apt-get update
RUN apt-get install -y bitcoind

RUN mkdir -p /btc/data \
    && echo "rpcuser=user\nrpcpassword=pass\nport=12333\nrpcport=12332\n" > /btc/bitcoin.conf \
    && echo "alias rt='bitcoin-cli -conf=/btc/bitcoin.conf -regtest'" >> ~/.bashrc

RUN mkdir /etc/service/bitcoind \
    && echo "#!/bin/bash\necho -e \$BITCOIN_CONF >> /btc/bitcoin.conf\n/usr/bin/bitcoind -conf=/btc/bitcoin.conf -datadir=/btc/data \$BITCOIND_PARAM\n" > /etc/service/bitcoind/run \
    && chmod +x /etc/service/bitcoind/run

# disable sshd
RUN rm -rf /etc/service/sshd

EXPOSE 12333 12332
CMD ["/sbin/my_init"]
