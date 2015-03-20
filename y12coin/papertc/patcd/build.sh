#!/bin/bash

set -e
set -x

cd ~/tmp/bitcoin
make -j4
make install-strip
