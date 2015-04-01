```
$ source alias.sh
$ dc build bitcore
$ dc run bitcore node -v
v0.10.33
$ dc run bitcore npm -v
1.4.28

$ dc run bitcore node /app/mnemonic.js
{ name: 'Redtcd',
  alias: 'Redtcd',
  pubkeyhash: 140,
  privatekey: 107,
  scripthash: 125,
  xpubkey: 76067358,
  xprivkey: 76066276,
  networkMagic: <Buffer fa bf b5 da>,
  port: 18333,
  dnsSeeds: [] }
about gravity ritual reward symbol leisure fence autumn nut pledge increase electric
<HDPrivateKey: xprv9s21ZrQH143K3UufQSRc4xugakdgoRzxzUct2oJGyAXNPGbJ4xpE6wgWKCCGxEdJtRdeerY6yBHXYn6Jqt6TtPLBK1vq7MxEPUM7CvGPWX7>

$ dc run bitcore npm list
/app
├─┬ bitcore-mnemonic@0.10.1
│ └─┬ bitcore@0.11.6
│   ├── bn.js@0.16.1
│   ├── bs58@2.0.0
│   ├─┬ elliptic@0.16.0
│   │ └── brorand@1.0.1
│   ├── hash.js@0.3.2
│   ├── inherits@2.0.1
│   ├── lodash@2.4.1
│   └── sha512@0.0.1
└─┬ bitcore-p2p@0.11.2
  ├─┬ bitcore@0.11.6
  │ ├── bn.js@0.16.1
  │ ├── bs58@2.0.0
  │ ├─┬ elliptic@0.16.0
  │ │ └── brorand@1.0.1
  │ ├── hash.js@0.3.2
  │ ├── inherits@2.0.1
  │ ├── lodash@2.4.1
  │ └── sha512@0.0.1
  ├── bloom-filter@0.2.0
  ├── buffers@0.1.1
  └─┬ socks5-client@0.3.6
    ├─┬ ipv6@3.1.1
    │ ├─┬ cli@0.4.5
    │ │ └─┬ glob@5.0.3
    │ │   ├─┬ inflight@1.0.4
    │ │   │ └── wrappy@1.0.1
    │ │   ├── inherits@2.0.1
    │ │   ├─┬ minimatch@2.0.4
    │ │   │ └─┬ brace-expansion@1.1.0
    │ │   │   ├── balanced-match@0.2.0
    │ │   │   └── concat-map@0.0.1
    │ │   └─┬ once@1.3.1
    │ │     └── wrappy@1.0.1
    │ ├─┬ cliff@0.1.10
    │ │ ├── colors@1.0.3
    │ │ ├── eyes@0.1.8
    │ │ └─┬ winston@0.8.3
    │ │   ├── async@0.2.10
    │ │   ├── colors@0.6.2
    │ │   ├── cycle@1.0.3
    │ │   ├── isstream@0.1.2
    │ │   ├── pkginfo@0.3.0
    │ │   └── stack-trace@0.0.9
    │ └── sprintf@0.1.5
    └── network-byte-order@0.2.0
```
