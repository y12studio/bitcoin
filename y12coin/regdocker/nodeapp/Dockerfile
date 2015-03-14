FROM y12docker/pbase:15.03
WORKDIR /bnode
RUN npm install -g node-static
RUN npm install bitcore
ADD regtest.js /bnode/
# install build-build-essential for bitcore-node/node-gyp rebuild failed.
RUN apt-get update
RUN apt-get install -yq build-essential
# bitpay/bitcore-node  https://github.com/bitpay/bitcore-node
RUN git clone https://github.com/bitpay/bitcore-node && cd bitcore-node \
   && npm install

EXPOSE 8080
CMD ["static"]
