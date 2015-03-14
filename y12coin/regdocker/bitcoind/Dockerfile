FROM y12docker/pbase:15.03

RUN apt-get -y update
RUN apt-get install -y python-software-properties

RUN add-apt-repository ppa:bitcoin/bitcoin
RUN apt-get update
RUN apt-get install -y bitcoind

RUN mkdir -p /btc/data \
    && echo "rpcuser=user\nrpcpassword=pass\naddnode=seeda\naddnode=seedb\n" > /btc/bitcoin.conf \
    && echo "alias rt='bitcoin-cli -conf=/btc/bitcoin.conf -regtest'" >> ~/.bashrc

RUN mkdir /etc/service/bitcoind \
    && echo "#!/bin/bash\n/usr/bin/bitcoind -conf=/btc/bitcoin.conf -datadir=/btc/data \$BITCOIND_PARAM\n" > /etc/service/bitcoind/run \
    && chmod +x /etc/service/bitcoind/run

# disable sshd
RUN rm -rf /etc/service/sshd

EXPOSE 18332 18444
CMD ["/sbin/my_init"]
