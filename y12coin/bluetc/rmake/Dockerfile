FROM bluetc_rbase
RUN apk-install build-base
RUN apk-install boost-dev openssl-dev db-dev miniupnpc-dev@testing protobuf-dev libqrencode-dev autoconf automake libtool

ENV SRC_DIR /root/bitcoin

RUN wget -qO- https://github.com/bitcoin/bitcoin/archive/v0.10.0.tar.gz | tar xvz -C /tmp
RUN mv /tmp/bitcoin-* $SRC_DIR

RUN apk-install linux-headers

RUN cd $SRC_DIR && ./autogen.sh \
    && ./configure \
		--prefix=/usr \
		--with-incompatible-bdb \
		--disable-ccache \
        --disable-static \
        -disable-tests --without-gui \
    && make && make install
