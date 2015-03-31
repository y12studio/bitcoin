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
