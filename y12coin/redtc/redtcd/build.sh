#!/bin/bash

set -e
set -x

SCRIPTPATH=$( cd "$(dirname "$0")" ; pwd -P )
DIRBUILD=~/tmp/bitcoin

cd ${SCRIPTPATH} && python patch.py && python build-pycoin-yml.py

# apt-get -y update
# apt-get -yq install automake autoconf libtool pkg-config libboost-all-dev libdb5.1++-dev
# apt-get -yq install bsdmainutils libssl-dev
# download bitcoin src v0.10.0
# wget -qO- https://github.com/bitcoin/bitcoin/archive/v0.10.0.tar.gz | tar xvz -C ~/tmp
rm -rf ${DIRBUILD}
cp -r ~/tmp/bitcoin-0.10.0 ${DIRBUILD}
cd ${DIRBUILD}
patch -p1 < ${SCRIPTPATH}/patchfile.v2
./autogen.sh
CONFIGFLAGS="-disable-tests --without-gui --enable-upnp-default --disable-ccache --disable-maintainer-mode --disable-dependency-tracking"
./configure --prefix=${SCRIPTPATH} --with-incompatible-bdb ${CONFIGFLAGS}
make -j4
make install-strip
#
# larsks/dockerize https://github.com/larsks/dockerize
#
cd ${SCRIPTPATH}
dockerize -t redtcd -a bin/bitcoind /usr/bin/coind \
    -a bin/bitcoin-cli /usr/bin/coin-cli \
    -a bin/bitcoin-tx /usr/bin/coin-tx \
    -a bitcoin.conf /btc/coin.conf \
    -a README.md /btc/data/README.md \
    -a /bin/bash /bin/bash \
    -a /bin/echo /bin/echo \
    -a bashrc /bashrc \
    -c /bin/bash --filetools
