TODO build private key

build genesis block

Wed Mar 11 18:58:56 CST 2015

```
$ python genesis.py -z "TestTimeStamp" -t 1317972665                                                                       ==== options ====
{'nonce': 0, 'timestamp': 'TestTimeStamp', 'pubkey': '04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f', 'value': 5000000000, 'time': 1317972665}
04ffff001d01040d5465737454696d655374616d70

==== block info ====
merkle hash: 560c7b16db437266520f3aa50dc7b9746d9138c65edc77fe5fb992c7b0236a25
pszTimestamp: TestTimeStamp
pubkey: 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
time: 1317972665
bits: 0x1e0ffff0

==== generate hash ====
Searching for genesis hash..
189170.0 hash/s, estimate: 0.0 h
==== genesis found ====
genesis hash found!
nonce: 923576
genesis hash: 000007e839b1459b9fb79c5a578709c1ae348f6240c2d5607799d4d86fdaacef
==== END ====


```


build bitcoind

Wed Mar 11 15:00:45 CST 2015

```
$ cat /etc/issue
Ubuntu 14.04.2 LTS
$ git branch
  master
* y12coin2015
$ sudo apt-get build-essential automake
$ sudo apt-get install autoconf libtool pkg-config libboost-all-dev libdb5.1++-dev
$ ./autogen.sh
$ ./configure --without-miniupnpc --disable-ipv6 --with-incompatible-bdb
$ make
$ sudo make install

libtool: install: /usr/bin/install -c bitcoind /usr/local/bin/bitcoind
libtool: install: /usr/bin/install -c bitcoin-cli /usr/local/bin/bitcoin-cli
libtool: install: /usr/bin/install -c bitcoin-tx /usr/local/bin/bitcoin-tx
libtool: install: /usr/bin/install -c test/test_bitcoin /usr/local/bin/test_bitcoin

$ cp y12coin/bitcoin.conf.tpl ~/.bitcoin/bitcoin.conf
$ cat ~/.bitcoin/bitcoin.conf

testnet=0
rpcuser=bitcoinrpc
rpcpassword=GyiRE3tX4qwH8bru47goy44zVhNF2NPiwcagGqpBCB5X

$ bitcoin-cli --version
Bitcoin Core RPC client version v0.10.99.0-affb4d8-dirty
$ bitcoind &
[1] 28549
$ bitcoin-cli getblockcount
2461
$ bitcoin-cli getinfo
{
    "version" : 109900,
    "protocolversion" : 70002,
    "blocks" : 4845,
    "timeoffset" : -1,
    "connections" : 8,
    "proxy" : "",
    "difficulty" : 1.00000000,
    "testnet" : false,
    "relayfee" : 0.00001000,
    "errors" : "This is a pre-release test build - use at your own risk - do not use for mining or merchant applications"
}
```

Wed Mar 11 14:50:23 CST 2015

```
$ git checkout master
$ git branch
* master
$ git checkout -b y12coin2015
$ git branch
  master
* y12coin2015
$ git status
On branch y12coin2015
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   contrib/y12coin/README.md
$ git commit -m 'create branch y12coin2015'
$ git push origin y12coin2015
```

[Syncing a fork - User Documentation](https://help.github.com/articles/syncing-a-fork/)

```
$ git remote -v
origin  git@github.com:y12studio/y12bitcoin.git (fetch)
origin  git@github.com:y12studio/y12bitcoin.git (push)
upstream        https://github.com/bitcoin/bitcoin.git (fetch)
upstream        https://github.com/bitcoin/bitcoin.git (push)


$ git fetch upstream
$ git checkout master
$ git merge upstream/master
