FROM y12docker/pbase_be:15.03

RUN apt-get -y update
RUN apt-get -yq install automake autoconf libtool pkg-config libboost-all-dev libdb5.1++-dev
RUN apt-get -yq install bsdmainutils libssl-dev

WORKDIR /opt/butcd

RUN wget -qO- https://github.com/bitcoin/bitcoin/archive/v0.10.0.tar.gz | tar xvz -C /tmp &&\
    mv /tmp/bitcoin-* /opt/butcd/bitcoin

RUN cd bitcoin && ./autogen.sh \
    && ./configure --without-miniupnpc --disable-ipv6 --with-incompatible-bdb

# RUN sed xxx

RUN cd bitcoin \
    && make \
    && make install

# disable sshd
RUN rm -rf /etc/service/sshd
RUN rm -f /etc/my_init.d/00_regen_ssh_host_keys.sh

EXPOSE 12333 12332
CMD ["/sbin/my_init"]
