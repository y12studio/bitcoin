Mon Apr  6 20:48:34 CST 2015
```
$ dcup

alice uses an image, skipping
test uses an image, skipping
Recreating redtc_seeda_1...
Recreating redtc_seedb_1...
Recreating redtc_bitcore_1...
Recreating redtc_bob_1...
Recreating redtc_pycoin_1...
Recreating redtc_alice_1...
Recreating redtc_test_1...
Attaching to redtc_test_1, redtc_alice_1, redtc_pycoin_1, redtc_bob_1, redtc_bitcore_1, redtc_seedb_1, redtc_seeda_1
test_1    | test_http.TestWebRequest.test_alice ... ok
test_1    | test_http.TestWebRequest.test_bob ... ok
test_1    | test_http.TestWebRequest.test_seeda ... ok
test_1    |
test_1    | ----------------------------------------------------------------------
test_1    | Ran 3 tests in 3.041s
test_1    |
test_1    | OK
redtc_test_1 exited with code 0
```


Thu Apr  2 18:45:40 CST 2015

```
$ docker images | grep redtc
redtc_bitcore       latest              d7b56852bf26        20 minutes ago      29.49 MB
redtc_pycoin        latest              d8cb0a2ed801        44 hours ago        69.38 MB
redtcd              latest              04a21ebe5e4e        2 days ago          17.56 MB
```

Tue Mar 31 22:31:45 CST 2015

```
$ source alias.sh
$ dc build pycoin
$ dc run pycoin ku -h
$ pku -h
usage: ku [-h] [-w] [-W] [-a] [-u] [-P] [-j] [-s SUBKEY]
          [-n {RTCD,BTC,XTN,LTC,XLT,VIA,TVI,DOGE,BC,DRK,tDRK,MEC,MYR,UNO,JBS,MZC,RIC}]
          [--override-network {RTCD,BTC,XTN,LTC,XLT,VIA,TVI,DOGE,BC,DRK,tDRK,MEC,MYR,UNO,JBS,MZC,RIC}]
          item [item ...]

Known networks codes: RTCD (Redtcd mainnet), BTC (Bitcoin mainnet), XTN
(Bitcoin testnet3), LTC (Litecoin mainnet), XLT (Litecoin testnet), VIA
(Viacoin mainnet), TVI (Viacoin testnet), DOGE (Dogecoin mainnet), BC
(Blackcoin mainnet), DRK (Darkcoin mainnet), tDRK (Darkcoin testnet), MEC
(Megacoin mainnet), MYR (Myriadcoin mainnet), UNO (Unobtanium mainnet), JBS
(Jumbucks mainnet), MZC (Mazacoin mainnet), RIC (Riecoin mainnet)

$ pku -n RTCD P:foo123


input                       : P:foo123
network                     : Redtcd mainnet
netcode                     : RTCD
wallet key                  : xprv9s21ZrQH143K2wxuiw6TsooaMS1UuSKEG2ecodKstjguqw88kHC7PA2Fg2wNrb\
                                VEUUrwmNwxUtpbLfvMX5PxPy8QaEZkpD5Wytq12c4N5fP
public version              : xpub661MyMwAqRbcFS3NpxdUEwkJuTqyJu35dFaDc1jVT5DtijTHHpWMvxLjXGRwmW\
                                GqxxVo5Nsykf39GytyzRiD3jQcGrV54M6rQaW8TFYLx7C
tree depth                  : 0
fingerprint                 : bcb3964b
parent f'print              : 00000000
child index                 : 0
chain code                  : 595f1d3f06d424ecb72f800678bc60fe5b1b3e0d06684b4ec8dbafa3a6ecec62
private key                 : yes
secret exponent             : 113203460196365794417836069566467237164431446589835561036208489629595376061019
 hex                        : fa46e34c6503a5f3785506efb3a458a8572946b0b19862b78d3dea08f0a88a5b
wif                         : GyRyW7Cv5XRc2gaHhQAi2wQTLFw54JjkzYxMFvVatk82ypSmbHDt
 uncompressed               : 4ctss6V5KhRc8BKsTNZZQYp15N4BtVwYiayVc6mzXJURU1ssxEw
public pair x               : 21593479522770990042883530725579673792864070234553897807505144510899602684277
public pair y               : 80351513151441525828983835173980861829332894676927270796314477149424804817608
 x as hex                   : 2fbd79ee9b261e9f74660206b7193e7d23b369f35c871222e9cfbe188ca17975
 y as hex                   : b1a55843fbd28ae6ba4526e836767042b75e355542ded8696774fc64226deac8
y parity                    : even
key pair as sec             : 022fbd79ee9b261e9f74660206b7193e7d23b369f35c871222e9cfbe188ca17975
 uncompressed               : 042fbd79ee9b261e9f74660206b7193e7d23b369f35c871222e9cfbe188ca17975\
                                b1a55843fbd28ae6ba4526e836767042b75e355542ded8696774fc64226deac8
hash160                     : bcb3964bd40a74a4c0b0b2eef7b25b523e246973
 uncompressed               : bd2b236ed1232fd12ca91bdb993a52e804578b12
Redtcd address              : ydXD2CPpvZ7rEJ9mozneQHDVRU5K965YGU
Redtcd address uncompressed : ydZgEmWfnMJHeU9B5fiVhEAyWCCbzitCAV

```


Tue Mar 31 16:55:09 CST 2015

```
$ source alias.sh
$ dcup
$ dc ps
      Name             Command             State              Ports
-------------------------------------------------------------------------
redtc_alice_1      /usr/bin/coind     Up                 12332/tcp,
                   -regtest -c ...                       12333/tcp
redtc_bob_1        /usr/bin/coind     Up                 12332/tcp,
                   -regtest -c ...                       12333/tcp
redtc_seeda_1      /usr/bin/coind     Up                 12332/tcp,
                   -regtest -t ...                       12333/tcp
redtc_seedb_1      /usr/bin/coind     Up                 12332/tcp,
                   -regtest -t ...                       12333/tcp
$ alicesh

bash-4.3# source bashrc
bash-4.3# ccli getinfo
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
    "keypoololdest" : 1427796277,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}

bash-4.3# ccli getpeerinfo
[
    {
        "id" : 1,
        "addr" : "172.17.0.51:12333",
        "services" : "0000000000000001",
        "lastsend" : 1427796278,
        "lastrecv" : 1427796278,
        "bytessent" : 337,
        "bytesrecv" : 245,
        "conntime" : 1427796278,
        "pingtime" : 0.15259300,
        "version" : 70002,
        "subver" : "/SatoshiREDtcd:0.10.0/",
        "inbound" : false,
        "startingheight" : 0,
        "banscore" : 0,
        "synced_headers" : -1,
        "synced_blocks" : -1,
        "inflight" : [
        ],
        "whitelisted" : false
    },
    {
        "id" : 2,
        "addr" : "172.17.0.55:12333",
        "services" : "0000000000000001",
        "lastsend" : 1427796278,
        "lastrecv" : 1427796278,
        "bytessent" : 269,
        "bytesrecv" : 313,
        "conntime" : 1427796278,
        "pingtime" : 0.04177600,
        "version" : 70002,
        "subver" : "/SatoshiREDtcd:0.10.0/",
        "inbound" : false,
        "startingheight" : 0,
        "banscore" : 0,
        "synced_headers" : -1,
        "synced_blocks" : -1,
        "inflight" : [
        ],
        "whitelisted" : false
    }
]

bash-4.3# ccli setgenerate true 15

bash-4.3# ccli getinfo
{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 1120.00000000,
    "blocks" : 15,
    "timeoffset" : 0,
    "connections" : 0,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1427795140,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}


```
