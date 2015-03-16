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
