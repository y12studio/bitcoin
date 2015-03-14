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
