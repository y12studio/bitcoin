#!/bin/bash

set -e
set -x

SCRIPTPATH=$( cd "$(dirname "$0")" ; pwd -P )
cd ~/tmp/bitcoin-*
CONFIGFLAGS="--enable-upnp-default --enable-glibc-back-compat --enable-reduce-exports LDFLAGS=-static-libstdc++ --disable-ccache --disable-maintainer-mode --disable-dependency-tracking"
./configure --prefix=${SCRIPTPATH} -disable-tests --without-gui --with-incompatible-bdb ${CONFIGFLAGS}
make -j4
make install-strip
cd ${SCRIPTPATH} && docker build -t y12docker/xbutcd .
