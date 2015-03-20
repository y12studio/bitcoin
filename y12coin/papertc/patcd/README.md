Fri Mar 20 21:14:17 CST 2015

build patch file

```
$ git clone -b v0.10.0 --single-branch https://github.com/bitcoin/bitcoin
$ cd bitcoin
$ git checkout -b patcd
Switched to a new branch 'patcd'
$ git status
On branch patcd
nothing to commit, working directory clean

$ vi/nano/.....
$ git status
On branch patcd
Changes not staged for commit:
        modified:   src/bitcoin-cli.cpp
        modified:   src/bitcoin-tx.cpp
        modified:   src/bitcoind.cpp
        modified:   src/chainparams.cpp
        modified:   src/main.cpp
        modified:   src/main.h
        modified:   src/qt/transactionrecord.h
        modified:   src/script/standard.h


$ git diff > ~/git/y12bitcoin/y12coin/papertc/patcd/patchfile.v1

$ alias chome='cd ~/git/y12bitcoin/y12coin/papertc/patcd'
$ chome && ./install.sh
$ cd ~/tmp/bitcoin/ && patch -p1 < ~/git/y12bitcoin/y12coin/papertc/patcd/patchfile.v1
$ chome && ./build.sh
$ cd .. && dcup

$ alicesh

root@155cf47c9015:/# bitcoind --version
PATCD_NAME Daemon version v0.10.0.0-g047a898

root@155cf47c9015:/# bitcoin-cli --version
PATCD_NAME RPC client version v0.10.0.0-g047a898

root@155cf47c9015:/# rt getinfo
{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 0.00000000,
    "blocks" : 0,
    "timeoffset" : 0,
    "connections" : 2,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1426858891,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}

root@544f163dcb6e:/# rt getnewaddress
yS95TdzaxvVJTCfTsMoz9GAfo82kVcSviF

root@544f163dcb6e:/# rt setgenerate true 1
[
    "1f3c26b886377d4a7f4b4c518d99ee5ebb7fdb8a972e71eb27d49e4537d79e5b"
]
root@544f163dcb6e:/# rt getbalance
0.00000000
root@544f163dcb6e:/# rt setgenerate true 10
[
    "11011b3b86fedd15c2c0ef8932a9c820c4536b5329ade423d85710d682aee8fe",
    "5422565b14d4715a2adb78aa4e65b512264c45b7434f7bd24db8697283e5fcc1",
    "27a0a053e6c78695fdd604baf4c530bab6ddd93136ef400f913625f94ca00cbd",
    "3b48cc9e925ca076aeca95ec80719266d41bbdcadeb724b52e3a4ffe0da6bcb5",
    "3524b6b56a0a10b744135755eee03c46e58f977b043b4e76f2d7f1d200a57b7d",
    "6d1a2dfd1dfb115dde32e983d572648e81f41dba529dfaaef82bd72e69648224",
    "375ace88a79c61ba41a6b2064733fb95aceb5eab55d65ee4a709562c6124cfa9",
    "75761d88b31118f5871fcd48556c27e107861406245563b4788384d1cd29a987",
    "19094b550657f969f00753263b97a4e8b7591448ef2bbec4a4db448a22e1635b",
    "2a16aa98ae7c4e6e2c94eea0ee0deb02e2ec883c538a0334e16f77b37696dead"
]
root@544f163dcb6e:/# rt getbalance
0.00000000

root@544f163dcb6e:/# rt setgenerate true 2
[
    "54b375dd32d77c114c308a754b9956309bc1fb2e3499baf2ee284b67663e20e8",
    "11430d10af76971ecd88a5aad59b39f1cdb47a49496d3e667fffa270057aa2ed"
]

root@544f163dcb6e:/# rt getinfo
{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 9999.00000000,
    "blocks" : 13,
    "timeoffset" : 0,
    "connections" : 2,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1426861449,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}

root@544f163dcb6e:/# rt setgenerate true 2 && rt getinfo
[
    "139c6a90f0f48cc22d37cf4d64ed9d2616af10a087b7de5b88ca76ce062f9872",
    "3e84734c47519693800fa81b921ae40142d50cb7fc02a12ac9b773cfa3e96266"
]
{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 11999.00000000,
    "blocks" : 15,
    "timeoffset" : 0,
    "connections" : 2,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1426861449,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}

```


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
