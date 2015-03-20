Fri Mar 20 09:06:32 CST 2015

```
$ source alias.sh
$ dcup
$ dc ps
     Name            Command      State           Ports
---------------------------------------------------------------
papertc_alice_1   /sbin/my_init   Up       12332/tcp, 12333/tcp
papertc_bob_1     /sbin/my_init   Up       12332/tcp, 12333/tcp
papertc_patcd_1   /bin/true       Exit 0
papertc_seeda_1   /sbin/my_init   Up       12332/tcp, 12333/tcp
papertc_seedb_1   /sbin/my_init   Up       12332/tcp, 12333/tcp
$ alicesh
root@00f6c042e656:/# rt getinfo
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
    "keypoololdest" : 1426822792,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}

root@9fc282cb9f3d:/# rt getpeerinfo
[
    {
        "id" : 1,
        "addr" : "172.17.0.80:12333",
        "services" : "0000000000000001",
        "lastsend" : 1426822918,
        "lastrecv" : 1426822918,
        "bytessent" : 331,
        "bytesrecv" : 239,
        "conntime" : 1426822918,
        "pingtime" : 0.11125600,
        "version" : 70002,
        "subver" : "/Satoshi:0.10.0/",
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
        "addr" : "172.17.0.86:12333",
        "services" : "0000000000000001",
        "lastsend" : 1426822918,
        "lastrecv" : 1426822919,
        "bytessent" : 263,
        "bytesrecv" : 307,
        "conntime" : 1426822918,
        "pingtime" : 0.10995500,
        "version" : 70002,
        "subver" : "/Satoshi:0.10.0/",
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

root@00f6c042e656:/# rt --version
Y12coin Patcd RPC client version v0.10.0.0-g047a898

```
