#!/bin/bash

set -e
set -x

# apt-get -y update
# apt-get -yq install automake autoconf libtool pkg-config libboost-all-dev libdb5.1++-dev
# apt-get -yq install bsdmainutils libssl-dev

SCRIPTPATH=$( cd "$(dirname "$0")" ; pwd -P )

# download bitcoin src v0.10.0
# wget -qO- https://github.com/bitcoin/bitcoin/archive/v0.10.0.tar.gz | tar xvz -C ~/tmp
rm -rf ~/tmp/bitcoin
cp -r ~/tmp/bitcoin-* ~/tmp/bitcoin
cd ~/tmp/bitcoin
patch -p1 < ${SCRIPTPATH}/patchfile.v2
./autogen.sh
CONFIGFLAGS="-disable-tests --without-gui --enable-upnp-default --disable-ccache --disable-maintainer-mode --disable-dependency-tracking"
./configure --prefix=${SCRIPTPATH} --with-incompatible-bdb ${CONFIGFLAGS}
