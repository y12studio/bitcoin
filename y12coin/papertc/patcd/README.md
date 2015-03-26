Thu Mar 26 20:21:02 CST 2015

```
$ source alias.sh
$ vi/nano src
$ cdhome
$ cd patcd && ./patchv1.sh && ./patchv2.sh && ./install.sh && ./build.sh
$ dcup
$ alicesh
root@fde3017808d5:/# rt getnetworkinfo
{
    "version" : 100000,
    "subversion" : "/SatoshiPatcd:0.10.0/",
    "protocolversion" : 70002,
    "localservices" : "0000000000000001",
    "timeoffset" : 0,
    "connections" : 2,
    "networks" : [
        {
            "name" : "ipv4",
            "limited" : false,
            "reachable" : false,
            "proxy" : ""
        },
        {
            "name" : "ipv6",
            "limited" : false,
            "reachable" : false,
            "proxy" : ""
        },
        {
            "name" : "onion",
            "limited" : false,
            "reachable" : false,
            "proxy" : ""
        }
    ],
    "relayfee" : 0.00001000,
    "localaddresses" : [
    ]
}

root@ec084a10bbe8:/patcd# ku -h
usage: ku [-h] [-w] [-W] [-a] [-u] [-P] [-j] [-s SUBKEY]
          [-n {PTD,BTC,XTN,LTC,XLT,VIA,TVI,DOGE,BC,DRK,tDRK,MEC,MYR,UNO,JBS,MZC,RIC}]
          [--override-network {PTD,BTC,XTN,LTC,XLT,VIA,TVI,DOGE,BC,DRK,tDRK,MEC,MYR,UNO,JBS,MZC,RIC}]
          item [item ...]

Crypto coin utility ku ("key utility") to show information about Bitcoin or
other cryptocoin data structures.

positional arguments:
  item                  a BIP0032 wallet key string; a WIF; a bitcoin address;
                        an SEC (ie. a 66 hex chars starting with 02, 03 or a
                        130 hex chars starting with 04); the literal string
                        "create" to create a new wallet key using strong
                        entropy sources; P:wallet passphrase (NOT
                        RECOMMENDED); H:wallet passphrase in hex (NOT
                        RECOMMENDED); secret_exponent (in decimal or hex); x,y
                        where x,y form a public pair (y is a number or one of
                        the strings "even" or "odd"); hash160 (as 40 hex
                        characters)

optional arguments:
  -h, --help            show this help message and exit
  -w, --wallet          show just Bitcoin wallet key
  -W, --wif             show just Bitcoin WIF
  -a, --address         show just Bitcoin address
  -u, --uncompressed    show output in uncompressed form
  -P, --public          only show public version of wallet keys
  -j, --json            output as JSON
  -s SUBKEY, --subkey SUBKEY
                        subkey path (example: 0H/2/15-20)
  -n {PTD,BTC,XTN,LTC,XLT,VIA,TVI,DOGE,BC,DRK,tDRK,MEC,MYR,UNO,JBS,MZC,RIC}, --network {PTD,BTC,XTN,LTC,XLT,VIA,TVI,DOGE,BC,DRK,tDRK,MEC,MYR,UNO,JBS,MZC,RIC}
                        specify network (default: BTC = Bitcoin)
  --override-network {PTD,BTC,XTN,LTC,XLT,VIA,TVI,DOGE,BC,DRK,tDRK,MEC,MYR,UNO,JBS,MZC,RIC}
                        override detected network type

Known networks codes: PTD (Patcd mainnet), BTC (Bitcoin mainnet), XTN (Bitcoin
testnet3), LTC (Litecoin mainnet), XLT (Litecoin testnet), VIA (Viacoin
mainnet), TVI (Viacoin testnet), DOGE (Dogecoin mainnet), BC (Blackcoin
mainnet), DRK (Darkcoin mainnet), tDRK (Darkcoin testnet), MEC (Megacoin
mainnet), MYR (Myriadcoin mainnet), UNO (Unobtanium mainnet), JBS (Jumbucks
mainnet), MZC (Mazacoin mainnet), RIC (Riecoin mainnet)

root@aef84a4469bb:/patcd# ku -n PTD create

input                      : create
network                    : Patcd mainnet
netcode                    : PTD
wallet key                 : xprv9s21ZrQH143K3aMYAYjJCQNMphaugq6rgvKdz6YJvsaB8dUS3FyPVCEGqpWgun\
                               sgjRbkERYspDVUpKnj5wQRRakmvnFCZQTWpPdR3bHvJr9
public version             : xpub661MyMwAqRbcG4S1GaGJZYK6NjRQ6Hpi49FEnUwvVD7A1RoaaoHe2zYkh4Heoc\
                               v6BuwbhC2jNFc3RKkg7ZXcoALzt6ZxSthTpP8eA261WRu
tree depth                 : 0
fingerprint                : 5520e047
parent f'print             : 00000000
child index                : 0
chain code                 : 9863e79288a68a0fa6f8ed522551129b7994619f0e1773cc4bdbb03da12dd808
private key                : yes
secret exponent            : 94598197286997182882913828729041145067164255403105227081908076462644312927812
 hex                       : d124aea8356ebb90679f188507bab13d94b12d12be158b3cf61e7b59832bee44
wif                        : Gx41v8xXVXCCScg6SF55Lf3v7QAXAUaXBJ23abjnMykpscUBVoz1
 uncompressed              : 4camAKZyJLXdaSkkNaYjftfiwTzthD93m28wWN1dZPpzX9FW9EB
public pair x              : 19827663998100767690797009088710332879372605993821048514051075564243806741372
public pair y              : 9440145612143168755389028921873953622883249182490139025550645649128993729508
 x as hex                  : 2bd60f648e20e07994c21690fd28c680f0fab24b02e55b769ee7074153fe637c
 y as hex                  : 14deeeddadf14be5fe3a346cd7f65467663d4f5c62d90b9338bdead0a0ae2be4
y parity                   : even
key pair as sec            : 022bd60f648e20e07994c21690fd28c680f0fab24b02e55b769ee7074153fe637c
 uncompressed              : 042bd60f648e20e07994c21690fd28c680f0fab24b02e55b769ee7074153fe637c\
                               14deeeddadf14be5fe3a346cd7f65467663d4f5c62d90b9338bdead0a0ae2be4
hash160                    : 5520e04796502c6ff35adde82c4e5b9971c73b2c
 uncompressed              : a2451736df7c4353ffa6aab6a89336afcb038d95
Patcd address              : yU5ZfnAmjD2Dt9wtYH27ZfhrRZiMnGcQM8
Patcd address uncompressed : yb7T5nSWa8d7WLLxFk5P1MjuD22uFhoGDb


root@aef84a4469bb:/patcd# ku -n PTD P:foo

input                      : P:foo
network                    : Patcd mainnet
netcode                    : PTD
wallet key                 : xprv9s21ZrQH143K31AgNK5pyVvW23gHnkBq2wh5aEk6g1s496M8ZMjxncCKZKgb5j\
                               ZoY5eSJMJ2Vbyvi2hbmQnCuHBujZ2WXGTux1X2k9Krdtq
public version             : xpub661MyMwAqRbcFVF9ULcqLdsEa5WnCCugQAcgNd9iEMQ31tgH6u4DLQWoQayvtS\
                               VYFvXz2vPPpbXE1qpjoUFidhjFj82pVShWu9curWmb2zy
tree depth                 : 0
fingerprint                : 5d353a2e
parent f'print             : 00000000
child index                : 0
chain code                 : 5eeb1023fd6dd1ae52a005ce0e73420821e1d90e08be980a85e9111fd7646bbc
private key                : yes
secret exponent            : 65825730547097305716057160437970790220123864299761908948746835886007793998275
 hex                       : 91880b0e3017ba586b735fe7d04f1790f3c46b818a2151fb2def5f14dd2fd9c3
wif                        : GuvN2tXqZAFZNJZtJHEj6VrfBBiPqVyuQZ1c7XWdfo4w1fd2mhab
 uncompressed              : 4c6kHHfFdHbZi5S86GuxJZNDjBar8N4q89cUtmyZKkyAyPuxENM
public pair x              : 81821982719381104061777349269130419024493616650993589394553404347774393168191
public pair y              : 58994218069605424278320703250689780154785099509277691723126325051200459038290
 x as hex                  : b4e599dfa44555a4ed38bcfff0071d5af676a86abf123c5b4b4e8e67a0b0b13f
 y as hex                  : 826d8b4d3010aea16ff4c1c1d3ae68541d9a04df54a2c48cc241c2983544de52
y parity                   : even
key pair as sec            : 02b4e599dfa44555a4ed38bcfff0071d5af676a86abf123c5b4b4e8e67a0b0b13f
 uncompressed              : 04b4e599dfa44555a4ed38bcfff0071d5af676a86abf123c5b4b4e8e67a0b0b13f\
                               826d8b4d3010aea16ff4c1c1d3ae68541d9a04df54a2c48cc241c2983544de52
hash160                    : 5d353a2ecdb262477172852d57a3f11de0c19286
 uncompressed              : e5bd3a7e6cb62b4c820e51200fb1c148d79e67da
Patcd address              : yUpHTLdfrvMUHTUbfJDE1E69Thg96bL3rU
Patcd address uncompressed : yhGCGxY2PSJ29NhvKRFSv8QqdpbWPYTria

root@aef84a4469bb:/patcd# ku -n PTD P:foo -P -j
{
   "PTD_address": "yUpHTLdfrvMUHTUbfJDE1E69Thg96bL3rU",
   "PTD_address_uncompressed": "yhGCGxY2PSJ29NhvKRFSv8QqdpbWPYTria",
   "address": "yUpHTLdfrvMUHTUbfJDE1E69Thg96bL3rU",
   "address_uncompressed": "yhGCGxY2PSJ29NhvKRFSv8QqdpbWPYTria",
   "chain_code": "5eeb1023fd6dd1ae52a005ce0e73420821e1d90e08be980a85e9111fd7646bbc",
   "child_index": "0",
   "fingerprint": "5d353a2e",
   "hash160": "5d353a2ecdb262477172852d57a3f11de0c19286",
   "hash160_uncompressed": "e5bd3a7e6cb62b4c820e51200fb1c148d79e67da",
   "input": "P:foo",
   "key_pair_as_sec": "02b4e599dfa44555a4ed38bcfff0071d5af676a86abf123c5b4b4e8e67a0b0b13f",
   "key_pair_as_sec_uncompressed": "04b4e599dfa44555a4ed38bcfff0071d5af676a86abf123c5b4b4e8e67a0b0b13f826d8b4d3010aea16ff4c1c1d3ae68541d9a04df54a2c48cc241c2983544de52",
   "netcode": "PTD",
   "network": "Patcd mainnet",
   "parent_fingerprint": "00000000",
   "private_key": "no",
   "public_pair_x": "81821982719381104061777349269130419024493616650993589394553404347774393168191",
   "public_pair_x_hex": "b4e599dfa44555a4ed38bcfff0071d5af676a86abf123c5b4b4e8e67a0b0b13f",
   "public_pair_y": "58994218069605424278320703250689780154785099509277691723126325051200459038290",
   "public_pair_y_hex": "826d8b4d3010aea16ff4c1c1d3ae68541d9a04df54a2c48cc241c2983544de52",
   "tree_depth": "0",
   "wallet_key": "xpub661MyMwAqRbcFVF9ULcqLdsEa5WnCCugQAcgNd9iEMQ31tgH6u4DLQWoQayvtSVYFvXz2vPPpbXE1qpjoUFidhjFj82pVShWu9curWmb2zy",
   "y_parity": "even"
}

```

Sat Mar 21 14:45:34 CST 2015

new patch file

```
$ source alias.sh
$ cd bsrc
$ vi/nano/echo....
modified:   src/bitcoin-cli.cpp
modified:   src/bitcoin-tx.cpp
modified:   src/bitcoind.cpp
modified:   src/chainparams.cpp
modified:   src/main.cpp
modified:   src/main.h
modified:   src/primitives/block.h
modified:   src/qt/transactionrecord.h
modified:   src/script/standard.h
$ cdhome && patcd/patchv1.sh
$ vi/nano patcd/coin.conf
$ patcd/patchv2.sh
$ patcd/install.sh && patcd/build.sh
$ dcup
$ alicesh

root@eff1946ebdda:/# rt getinfo
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
    "keypoololdest" : 1426932232,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}

root@eff1946ebdda:/# bitcoin-cli --version
Bitcoin/Patcd/v150321 RPC client version v0.10.0.0-g047a898

root@eff1946ebdda:/# rt setgenerate true 15
[
    "7759eccfd2021b8ced5d176ae6ab6f8d2edcf2458ea63dbe487a77a6c070ba5f",
    "0e642e15343246941a67a16dfd6c5a75552595a79377b492c285a47d6f0864e8",
    "755329408ff6a08e6336000be72eb99a00f1b1688a7a5962d384e36fb46ba193",
    "31d0b970802980507efe64cb81eb4b0d0bdbf0fdc4ea8cf41706cf362982721a",
    "55b4f1f41c496a65f8096793190bd59118516a5f4bb1ea0d75f5041d4ff439ef",
    "3a941e753e3a59873be07eecb8922405c47e904afc8c25e72f60e751a99bd626",
    "0793c8521a9b2d786bad1e994c3bde40fbb3c62d73318ac5172887aff39aabc6",
    "7b0e3f9328c2f7d9a65ed529e519c5ec680aac48fff8c529f9eee8027e01cdee",
    "7fb8d2915ccee8aff57df629b7062a072a338b2baa33ab37541c895bbea4df5f",
    "14fb4682e351de663a095f230d4cc1dce6037dde61034d7b8422e3055aef18e1",
    "330cdf22ab354032692aff9e21ec06cb55a2d356e9edd163046e9d14781c62df",
    "204ed6e9507b30d28235a08fb35da0851ee2ae3a3bd6acadb91eb47edb8c2ab7",
    "74fe3e2b60a1de1883353a083174f0ce0f7f7434abb7b609c6912917604319e8",
    "2d5c0175a979b4a67a769a388d5367539177721501260065010314f4e11834ba",
    "3271eca0dfef77fbca8531dc11d52ec2edca97c0041a257da3c7d9dd934213fb"
]
root@eff1946ebdda:/# rt getinfo
{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 1120.00000000,
    "blocks" : 15,
    "timeoffset" : 0,
    "connections" : 2,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1426932232,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}

//Y_SUBSIDY|60
//Y_PREMINE_HEIGHT_1|1000
//Y_COINBASE_MATURITY|12
100+60*2

root@eff1946ebdda:/# rt getnewaddress
ygnFWS978mi96mUcSSWSadakys5v1Yvsec
root@eff1946ebdda:/# rt dumpprivkey ygnFWS978mi96mUcSSWSadakys5v1Yvsec
GvmVaRuPdnFf8pfbUdZZgy3HpaZKT8AaMZeS1Mc1T8M55c5FV62C

root@eff1946ebdda:~# rt listaccounts
{
    "" : 1120.00000000
}



```


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
