#!/bin/bash

set -e
set -x

# apt-get -y update
# apt-get -yq install automake autoconf libtool pkg-config libboost-all-dev libdb5.1++-dev
# apt-get -yq install bsdmainutils libssl-dev

# download bitcoin src v0.10.0
wget -qO- https://github.com/bitcoin/bitcoin/archive/v0.10.0.tar.gz | tar xvz -C ~/tmp
cd ~/tmp/bitcoin-*
./autogen.sh
