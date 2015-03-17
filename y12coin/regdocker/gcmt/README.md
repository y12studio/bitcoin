Tue Mar 17 09:41:40 CST 2015

```
$ gcmtsh

# Generate 101 blocks using a special version of the setgenerate RPC which is only available in regtest mode.
#  https://bitcoin.org/en/developer-examples#regtest-mode

root@a6640c357b61:/# minerrt setgenerate true 102 && minerrt getinfo

{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 100.00000000,
    "blocks" : 102,
    "timeoffset" : 0,
    "connections" : 1,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1426563624,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}

root@4da77c53a34b:/# bobrt getnewaddress && alicert getnewaddress

mpTbjYa54fJetgYCwAkANdsnqBeV9axcoS
mgvFiRugk47dxfbk3NroLyhbdLxHx1yyQD

minerrt sendtoaddress mpTbjYa54fJetgYCwAkANdsnqBeV9axcoS 2
minerrt setgenerate true 1
minerrt sendtoaddress mgvFiRugk47dxfbk3NroLyhbdLxHx1yyQD 3
minerrt setgenerate true 1
bobrt getinfo && alicert getinfo

{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 2.00000000,
    "blocks" : 104,
    "timeoffset" : 0,
    "connections" : 2,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1426563626,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}
{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 3.00000000,
    "blocks" : 104,
    "timeoffset" : 0,
    "connections" : 2,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1426563625,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}

alicert sendtoaddress mpTbjYa54fJetgYCwAkANdsnqBeV9axcoS 1.5 && minerrt setgenerate true 1
bobrt getinfo && alicert getinfo

{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 2.00000000,
    "blocks" : 105,
    "timeoffset" : 0,
    "connections" : 2,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1426563626,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}
{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 1.49999774,
    "blocks" : 105,
    "timeoffset" : 0,
    "connections" : 2,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1426563625,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}

# alicert listunspent && bobrt listunspent
[
]
[
    {
        "txid" : "6a5fb96321fb46fe8ad4c22f7428204a677fee46d3c7b337e8607a187271aa72",
        "vout" : 1,
        "address" : "mpTbjYa54fJetgYCwAkANdsnqBeV9axcoS",
        "account" : "",
        "scriptPubKey" : "76a9146216b89beb128737ac96d12920379dba0323a28888ac",
        "amount" : 2.00000000,
        "confirmations" : 3,
        "spendable" : true
    }
]

# minerrt setgenerate true 6
# alicert listunspent && bobrt listunspent
[
    {
        "txid" : "8fe9b05ae648ca6ca3d0d7a20e10fce87583004515c78b49f2e4cefea2d3692b",
        "vout" : 0,
        "address" : "mysFo5w2cVPbWsTzHtkPkeBf6j3VCAd5Ph",
        "scriptPubKey" : "76a914c949312b3e8b5ad022ce008c446a4341a72b2ecf88ac",
        "amount" : 1.49999774,
        "confirmations" : 6,
        "spendable" : true
    }
]
[
    {
        "txid" : "6a5fb96321fb46fe8ad4c22f7428204a677fee46d3c7b337e8607a187271aa72",
        "vout" : 1,
        "address" : "mpTbjYa54fJetgYCwAkANdsnqBeV9axcoS",
        "account" : "",
        "scriptPubKey" : "76a9146216b89beb128737ac96d12920379dba0323a28888ac",
        "amount" : 2.00000000,
        "confirmations" : 9,
        "spendable" : true
    },
    {
        "txid" : "8fe9b05ae648ca6ca3d0d7a20e10fce87583004515c78b49f2e4cefea2d3692b",
        "vout" : 1,
        "address" : "mpTbjYa54fJetgYCwAkANdsnqBeV9axcoS",
        "account" : "",
        "scriptPubKey" : "76a9146216b89beb128737ac96d12920379dba0323a28888ac",
        "amount" : 1.50000000,
        "confirmations" : 6,
        "spendable" : true
    }
]
```
