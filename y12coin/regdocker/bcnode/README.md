rename to bcnode

Mon Mar 16 09:44:54 CST 2015

```
$ dc up -d
$ bcnodesh
root@90654ba36418:/bnode/bitcore-node# cat config/default.yml
BitcoreNode:
  NetworkMonitor:
    network: regnet
    host: seeda
    port: 18444
LevelUp: ./db
RPC:
  username: user
  password: pass
  protocol: http
  host: 127.0.0.1
  port: 18332

root@90654ba36418:/bnode/bitcore-node# node index.js &

root@90654ba36418:/bnode/bitcore-node# curl http://localhost:3001
curl: (7) Failed to connect to localhost port 3001: Connection refused

root@90654ba36418:/bnode/bitcore-node# netstat -at
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 *:18444                 *:*                     LISTEN
tcp        0      0 localhost:18332         *:*                     LISTEN
tcp        0      0 90654ba36418:52281      bitreg_seeda_1:18444    ESTABLISHED
tcp        0      0 90654ba36418:52267      bitreg_seeda_1:18444    ESTABLISHED
tcp6       0      0 [::]:18444              [::]:*                  LISTEN
tcp6       0      0 localhost:18332         [::]:*                  LISTEN


```


Sat Mar 14 18:18:03 CST 2015

```
root@3d5fbd72c892:/bnode# ls
bitcore-node  node_modules  regtest.js

root@3d5fbd72c892:/bnode# node regtest.js
{ name: 'regnet',
  alias: 'regnet',
  pubkeyhash: 111,
  privatekey: 239,
  scripthash: 196,
  xpubkey: 70617039,
  xprivkey: 70615956,
  networkMagic: <Buffer fa bf b5 da>,
  port: 18333,
  dnsSeeds: [] }
cSziQcHNzV8V6WJoH3TA5LEKib2jEQwLghyqSEb5Aw6wxRFByZki
<Address: muZx1ym8z5Yg5TBcvMKEKHktMMyN6Cqh62, type: pubkeyhash, network: regnet>

root@3d5fbd72c892:/bnode# cd bitcore-node/
root@3d5fbd72c892:/bnode/bitcore-node# ls
CONTRIBUTING.md  api          http      node_modules  ws
LICENSE          config       index.js  package.json
README.md        gulpfile.js  lib       test
root@3d5fbd72c892:/bnode/bitcore-node# node index.js
Connection to bitcoind failed
root@3d5fbd72c892:/bnode/bitcore-node# cat config/default.yml
BitcoreNode:
  NetworkMonitor:
    network: livenet
    host: localhost
    port: 8333
LevelUp: ./db
RPC:
  username: username
  password: password
  protocol: http
  host: 127.0.0.1
  port: 8332

```
