FROM y12docker/pbase:15.03

RUN apt-get -y update
RUN apt-get install -y python-software-properties

RUN add-apt-repository ppa:bitcoin/bitcoin
RUN apt-get update
RUN apt-get install -y bitcoind

RUN mkdir ~/.bitcoin
RUN echo "rpcuser=test\nrpcpassword=test\naddnode=seed1\naddnode=seed2\n" > ~/.bitcoin/bitcoin.conf

RUN echo "alias rt='bitcoin-cli -regtest'" >> ~/.bashrc

EXPOSE 18332 18444
