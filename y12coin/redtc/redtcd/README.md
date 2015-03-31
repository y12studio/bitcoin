Tue Mar 31 16:08:27 CST 2015

```
$ ./build.sh
$ docker images | grep redtcd
redtcd              latest              cf291f882ae1        About a minute ago   16.46 MB
$ docker run redtcd coind --version
Bitcoin/REDtcd/v150321 Daemon version v0.10.0.0-g047a898
$ docker run redtcd coin-cli --version
Bitcoin/REDtcd/v150321 RPC client version v0.10.0.0-g047a898

$ docker run -i -t redtcd
# cat /btc/coin.conf
rpcuser=user
rpcpassword=pass
port=12333
rpcport=12332

$ docker run -d redtcd coind -conf=/btc/coin.conf -datadir=/btc/data
3e2dedce20e1112e08a88594db4d43efa8e7d3dd995fe944c1522cc02eba8f8a
$ docker exec 3e2dedce coin-cli -conf=/btc/coin.conf getinfo
{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 0.00000000,
    "blocks" : 0,
    "timeoffset" : 0,
    "connections" : 0,
    "proxy" : "",
    "difficulty" : 1.00000000,
    "testnet" : false,
    "keypoololdest" : 1427791623,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}
```
