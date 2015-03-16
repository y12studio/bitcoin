FROM bitreg_bitcoindbe
WORKDIR /bnode
RUN npm install bitcore
ADD regtest.js /bnode/
# bitpay/bitcore-node  https://github.com/bitpay/bitcore-node
RUN git clone --depth 1 https://github.com/bitpay/bitcore-node && cd bitcore-node \
   && npm install

ADD app.js /bnode/bitcore-node/
RUN cd /bnode/bitcore-node/ && sed -i '/var BitcoreNode/r app.js' index.js
#RUN cat /bnode/bitcore-node/index.js
ADD default.yml /bnode/bitcore-node/config/
#EXPOSE 8080
