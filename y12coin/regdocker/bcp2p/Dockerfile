FROM  bitreg_rbase
WORKDIR /bcp2p
RUN npm install bitcore bitcore-p2p bunyan
ADD beaver.conf /bcp2p/
ADD app.js /bcp2p/

# node app.js
RUN mkdir /etc/service/bcp2pd \
    && echo "#!/bin/bash\ncd /bcp2p && /usr/bin/node app.js\n" > /etc/service/bcp2pd/run \
    && chmod +x /etc/service/bcp2pd/run

# beaver -c beaver.conf -t tcp
RUN mkdir /etc/service/beaverd \
    && echo "#!/bin/bash\n/usr/local/bin/beaver -c /bcp2p/beaver.conf -t tcp\n" > /etc/service/beaverd/run \
    && chmod +x /etc/service/beaverd/run

CMD ["/sbin/my_init"]
