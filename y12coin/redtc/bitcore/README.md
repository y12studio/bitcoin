Thu Apr  2 17:04:12 CST 2015

```
$ source alias.sh
$ dc build bitcore
$ bccoin
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
{ wif: 'GuuEusHSedxA8YNfPQhqAgu9yWADHUyGxLRjHQCYEfmeEJcHF5f4',
  address: 'yQ7ycYGKgpBRKK1RPNvDiewfrqAQZU9h1E',
  pubkey: '02c27a387d7a4fb65a838ecb40fb11c4e6aa592bd1a00ac72b223e77f269fcbfe6',
  privkey: '90f42d879bb4c83ff85c032ba864cee2ad40c1ef2f4f47c5e86b035dd1b5f67c' }
{ mnemonic: 'whisper stereo exclude culture reject pact agent crime begin organ rack lawn',
  xprivkey: 'xprv9s21ZrQH143K4UY5zp18QsA5qAqPDszo1XnmhMijMRMxivT1adTNeg47XJyVd1gZzGHsVSCQfPNzn1DhdFhgeb7TiCcrAUpjn3Bu6S8uPAL',
  xpubkey: 'xpub661MyMwAqRbcGxcZ6qY8n16pPCfsdLieNkiNVk8LuktwbinA8AmdCUNbNYAeTan8TY2ttnWo9m9Q9QmXCApUR5ezkbocbbhnMQ3YBbdQ7XL',
  'ext/m/0h/0/99':
   { priv: 'xprv9yT93t6ZpgN4mc5UuAa5Adq1gWjA53rQvEwd7WfC3AvVvKF8v3ExpKue8RiS6wpNhZrpqiAC453fWM7Av4DhsUZgWgo7VmNU1G5zFoSkSVN',
     pub: 'xpub6CSVTPdTf3vMz69x1C75XmmkEYZeUWaGHTsDuu4obWTUo7aHTaZDN8E7yicnfPpZ5xAAfcMrXgkiBHcXpBqmyS3Ynbk6CtfRKE45biCAqfh',
     addr: 'yj2YVYYC5PfrTvn5aCiqqjBfpAG1iqdaAN' },
  'int/m/0h/1/99':
   { priv: 'xprv9yTsnznMM5eTeLQhu1ZTgaQ8MLHYGLFcT7YqxuHrZjaDCnYfg91BbEAkYwccTrmedH7DFx4ZKAj2KcZsQzcthPFe5WuekehafnuwfH8ZW1x',
     pub: 'xpub6CTECWKFBTCkrpVB136U3iLruN82fnyTpLUSmHhU857C5aspDgKS92VEQDhz4BRskLtxWVMF8JdW8ofjVb9LesYofWA6QMGhPvyy86rterN',
     addr: 'yh1RKAfNjUPynAZ4HZKk2Gg8bHXWwoE33Z' } }
```

test mnemonic.js

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
