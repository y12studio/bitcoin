FROM y12docker/pbase:15.03
WORKDIR /myapp
RUN npm install -g node-static
RUN npm install bitcore
ADD regtest.js /myapp/
EXPOSE 8080
CMD ["static"]
