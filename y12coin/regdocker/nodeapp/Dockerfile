FROM node:latest
WORKDIR /myapp
RUN npm install -g node-static
RUN npm install bitcore
ADD regtest.js /myapp/
EXPOSE 8080
