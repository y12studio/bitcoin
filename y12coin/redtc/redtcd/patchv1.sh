#!/bin/bash

set -e
set -x

SCRIPTPATH=$( cd "$(dirname "$0")" ; pwd -P )
BITCOINGIT=~/git/bitcoin
cd ~/git/bitcoin && git diff > ${SCRIPTPATH}/patchfile.v1
