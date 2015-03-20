Fri Mar 20 10:46:27 CST 2015

```
$ source alice.sh
$ cd patcd
$ chmod +x install.sh
$ ./install.sh
$ sed -i 's/Bitcoin Core Daemon/Y12coin Patcd Daemon/g' ~/tmp/bitcoin/src/bitcoind.cpp
$ sed -i 's/Bitcoin Core RPC client/Y12coin Patcd RPC client/g' ~/tmp/bitcoin/src/bitcoin-cli.cpp
$ chmod +x build.sh
$ ./build.sh
$ cd ..
$ dcup
$ alicesh
# bitcoind --version
Y12coin Patcd Daemon version v0.10.0.0-g047a898
Copyright (C) 2009-2015 The Bitcoin Core Developers
root@ae13cae7db3b:/# bitcoin-cli --version
Y12coin Patcd RPC client version v0.10.0.0-g047a898
```
