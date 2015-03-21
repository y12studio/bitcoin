#!/bin/bash

set -e
set -x

SCRIPTPATH=$( cd "$(dirname "$0")" ; pwd -P )
cd ${SCRIPTPATH} && cp patchfile.v1 patchfile.v2
cat coin.conf | sed '/^\#/d' | xargs -i sed -i 's|{}|' patchfile.v2
