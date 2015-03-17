FROM bitreg_bitcoind
# disable bitcoind
RUN rm -rf /etc/service/bitcoind

RUN echo "rpcuser=user\nrpcpassword=pass\nport=12333\nrpcport=12332\n" > /btc/rt.conf
RUN echo "alias alicert='bitcoin-cli -conf=/btc/rt.conf  -rpcconnect=alice -regtest'" >> ~/.bashrc
RUN echo "alias bobrt='bitcoin-cli -conf=/btc/rt.conf  -rpcconnect=bob -regtest'" >> ~/.bashrc
RUN echo "alias minerrt='bitcoin-cli -conf=/btc/rt.conf  -rpcconnect=miner -regtest'" >> ~/.bashrc
