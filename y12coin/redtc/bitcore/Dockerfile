FROM gliderlabs/alpine:3.1
RUN apk-install bash nodejs

WORKDIR /app

RUN npm install bitcore bitcore-mnemonic bitcore-p2p

ADD coin.js mnemonic.js /app/
