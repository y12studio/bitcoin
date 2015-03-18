[Creating your own experimental Bitcoin network | Gerald Kaszuba](https://geraldkaszuba.com/creating-your-own-experimental-bitcoin-network/)

[gak/docker-bitcoin-regtest](https://github.com/gak/docker-bitcoin-regtest)

TODO

[elasticsearch Repository | Docker Hub Registry - Repositories of Docker Images](https://registry.hub.docker.com/_/elasticsearch/)

Tue Mar 17 21:33:22 CST 2015

```
$ source alias.sh
$ dc up -d
$ dc logs

// browser http://docker_host:9200 and 9280

$ dc ps
      Name             Command             State              Ports
-------------------------------------------------------------------------
bitreg_alice_1     /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_bcnode_1    /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_bcp2p_1     /sbin/my_init      Up
bitreg_bitcoind_   /bin/true          Exit 0
1
bitreg_bitcoindb   /bin/true          Exit 0
e_1
bitreg_bob_1       /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_es_1        elasticsearch      Up                 0.0.0.0:9200->92
                                                         00/tcp, 9300/tcp
bitreg_gcmt_1      /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_kibana4_1   /bin/sh -c         Up                 0.0.0.0:9280->56
                   /run.sh                               01/tcp
bitreg_logsa_1     logstash agent     Up                 8333/tcp,
                   -f /loges/b ...                       9200/tcp,
                                                         9300/tcp
bitreg_miner_1     /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_rbase_1     /bin/true          Exit 0
bitreg_seeda_1     /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_seedb_1     /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
```

[bobrik/kibana4 Repository | Docker Hub Registry - Repositories of Docker Images](https://registry.hub.docker.com/u/bobrik/kibana4/)

Tue Mar 17 18:34:52 CST 2015

```
$ dc up -d
$ dc ps
      Name             Command             State              Ports
-------------------------------------------------------------------------
bitreg_alice_1     /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_bcnode_1    /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_bcp2p_1     /sbin/my_init      Up
bitreg_bitcoind_   /bin/true          Exit 0
1
bitreg_bitcoindb   /bin/true          Exit 0
e_1
bitreg_bob_1       /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_gcmt_1      /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_kibana4_1   /bin/sh -c         Up                 0.0.0.0:9280->56
                   /run.sh                               01/tcp
bitreg_loges_1     logstash agent     Up                 8333/tcp, 0.0.0.
                   -f /loges/b ...                       0:9200->9200/tcp
                                                         , 9300/tcp
bitreg_miner_1     /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_rbase_1     /bin/true          Exit 0
bitreg_seeda_1     /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_seedb_1     /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp

root@gcmt:/#
minerrt setgenerate true 101
minerrt sendtoaddress mpTbjYa54fJetgYCwAkANdsnqBeV9axcoS 1
minerrt setgenerate true 1
minerrt sendtoaddress mpTbjYa54fJetgYCwAkANdsnqBeV9axcoS 2
minerrt setgenerate true 1


browser http://docker_host:9280/

Error: This version of Kibana requires Elasticsearch 1.4.4 or higher on all nodes. I found the following incompatible nodes in your cluster:

Elasticsearch v1.1.1 @ inet[/172.17.1.37:9200] (172.17.1.37)

```


port=12333, rpcport=12444

Tue Mar 17 09:04:51 CST 2015

```
$ dc ps
      Name             Command             State              Ports
-------------------------------------------------------------------------
bitreg_alice_1     /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_bcnode_1    /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_bcp2p_1     /sbin/my_init      Up
bitreg_bitcoind_   /bin/true          Exit 0
1
bitreg_bitcoindb   /bin/true          Exit 0
e_1
bitreg_bob_1       /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_gcmt_1      /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_loges_1     logstash agent     Up                 8333/tcp, 0.0.0.
                   -f /loges/b ...                       0:9200->9200/tcp
                                                         , 9300/tcp
bitreg_rbase_1     /bin/true          Exit 0
bitreg_seeda_1     /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
bitreg_seedb_1     /sbin/my_init      Up                 12332/tcp,
                                                         12333/tcp
```

logstash added

Mon Mar 16 17:17:44 CST 2015

```
$ dc ps
      Name             Command             State              Ports
-------------------------------------------------------------------------
bitreg_alice_1     /sbin/my_init      Up                 18332/tcp,
                                                         18444/tcp
bitreg_bcnode_1    /sbin/my_init      Up                 18332/tcp,
                                                         18444/tcp
bitreg_bcp2p_1     /sbin/my_init      Up
bitreg_bitcoind_   /bin/true          Exit 0
1
bitreg_bitcoindb   /bin/true          Exit 0
e_1
bitreg_bob_1       /sbin/my_init      Up                 18332/tcp,
                                                         18444/tcp
bitreg_loges_1     logstash agent     Up                 9200/tcp,
                   -f /loges/b ...                       9292/tcp,
                                                         9300/tcp
bitreg_seeda_1     /sbin/my_init      Up                 18332/tcp,
                                                         18444/tcp
bitreg_seedb_1     /sbin/my_init      Up                 18332/tcp,
                                                         18444/tcp

```

rewrite

```
$ source alias.sh
$ dc build bitcoind && dc build bitcoindbe
$ dc build
$ dc up -d
$ dc ps
Name              Command      State           Ports
-------------------------------------------------------------------
bitreg_alice_1        /sbin/my_init   Up       18332/tcp, 18444/tcp
bitreg_bcnode_1       /sbin/my_init   Up       18332/tcp, 18444/tcp
bitreg_bcp2p_1        /sbin/my_init   Up
bitreg_bitcoind_1     /bin/true       Exit 0
bitreg_bitcoindbe_1   /bin/true       Exit 0
bitreg_bob_1          /sbin/my_init   Up       18332/tcp, 18444/tcp
bitreg_seeda_1        /sbin/my_init   Up       18332/tcp, 18444/tcp
bitreg_seedb_1        /sbin/my_init   Up       18332/tcp, 18444/tcp
```


rewrite docker-cimpose.yml

```
$ source alias.sh
$ dc build
$ dc up -d
Creating bitreg_seeda_1...
Creating bitreg_seedb_1...
Creating bitreg_bob_1...
Creating bitreg_nred_1...
Creating bitreg_alice_1...
Creating bitreg_bitcoind_1...
$ dc ps
      Name             Command      State           Ports
-----------------------------------------------------------------
bitreg_alice_1      /sbin/my_init   Up       18332/tcp, 18444/tcp
bitreg_bitcoind_1   /bin/true       Exit 0
bitreg_bob_1        /sbin/my_init   Up       18332/tcp, 18444/tcp
bitreg_nred_1       static          Up       8080/tcp
bitreg_seeda_1      /sbin/my_init   Up       18332/tcp, 18444/tcp
bitreg_seedb_1      /sbin/my_init   Up       18332/tcp, 18444/tcp

```

phusion/baseimage-docker runit test Sat Mar 14 16:48:52 CST 2015

```
$ source alias.sh
$ dc build
$ dc up -d

$ alicesh
root@59c7ac433eb5:/# rt getnewaddress
mgbsVjpqzyMo5qJLyRRoT36CJ3xi9g2tWp

$ bobsh

root@260555c43d16:/# ps -auwwwx
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.2  28812  8124 ?        Ss   08:31   0:00 /usr/bin/python3 -u /sbin/my_init
root        98  0.0  0.0    188    40 ?        S    08:31   0:00 /usr/bin/runsvdir -P /etc/service
root        99  0.0  0.0    168     4 ?        Ss   08:31   0:00 runsv bitcoind
root       100  0.0  0.0    168     4 ?        Ss   08:31   0:00 runsv syslog-ng
root       101  0.0  0.0    168     4 ?        Ss   08:31   0:00 runsv cron
root       102  0.0  0.0    168     4 ?        Ss   08:31   0:00 runsv syslog-forwarder
root       103  0.0  0.0   7472   616 ?        S    08:31   0:00 tail -f -n 0 /var/log/syslog
root       104  0.0  0.1  65748  4304 ?        S    08:31   0:00 syslog-ng -F -p /var/run/syslog-ng.pid --no-caps
root       105  0.0  0.0  26744  1116 ?        S    08:31   0:00 /usr/sbin/cron -f
root       106  0.0  0.0  21108  1560 ?        S    08:31   0:00 /bin/bash ./run
root       110  0.1  0.7 713520 31860 ?        SLl  08:31   0:00 /usr/bin/bitcoind -conf=/btc/bitcoin.conf -datadir=/btc/data -regtest
root       167  0.0  0.0  18164  1904 ?        S    08:45   0:00 bash
root       183  0.0  0.0  15564  1148 ?        R+   08:45   0:00 ps -auwwwx

# rt setgenerate true 101
# rt setgenerate true 10
# rt getinfo
{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 550.00000000,
    "blocks" : 111,
    "timeoffset" : 0,
    "connections" : 2,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1426321874,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}


$ seedash

root@7c78b325349c:/# ps -auwwwx
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1  28812  8080 ?        Ss   08:31   0:00 /usr/bin/python3 -u /sbin/my_init
root        95  0.0  0.0    188    32 ?        S    08:31   0:00 /usr/bin/runsvdir -P /etc/service
root        96  0.0  0.0    168     4 ?        Ss   08:31   0:00 runsv bitcoind
root        97  0.0  0.0    168     4 ?        Ss   08:31   0:00 runsv syslog-ng
root        98  0.0  0.0    168     4 ?        Ss   08:31   0:00 runsv cron
root        99  0.0  0.0    168     4 ?        Ss   08:31   0:00 runsv syslog-forwarder
root       100  0.0  0.0  26744  1112 ?        S    08:31   0:00 /usr/sbin/cron -f
root       101  0.0  0.1  65740  4308 ?        S    08:31   0:00 syslog-ng -F -p /var/run/syslog-ng.pid --no-caps
root       102  0.0  0.0  21080  1536 ?        S    08:31   0:00 /bin/bash ./run
root       103  0.0  0.0   7472   612 ?        S    08:31   0:00 tail -f -n 0 /var/log/syslog
root       105  0.1  0.7 717744 29772 ?        SLl  08:31   0:00 /usr/bin/bitcoind -conf=/btc/bitcoin.conf -datadir=/btc/data -regtest -txindex
root       132  0.0  0.0  18136  1980 ?        S    08:39   0:00 bash
root       152  0.0  0.0  15564  1148 ?        R+   08:44   0:00 ps -auwwwx

# ls /btc/data/regtest/
bitcoind.pid  chainstate  db.log     peers.dat
blocks        database    debug.log  wallet.dat

root@7c78b325349c:/# tail /btc/data/regtest/debug.log
2015-03-14 08:38:39 UpdateTip: new best=0dd34494c094245063f0b1ab1d9e60c5f42f32aafa07b6ad74ee2e915fec381e  height=103  log2_work=7.7004397  tx=104  date=2015-03-14 08:38:38 progress=1.000000  cache=103
2015-03-14 08:38:39 UpdateTip: new best=5a396331fdc72ebce13e09ea942e32dbaebdd50f6bd2b30555d5a516931485fd  height=104  log2_work=7.7142455  tx=105  date=2015-03-14 08:38:38 progress=1.000000  cache=104
2015-03-14 08:38:39 UpdateTip: new best=222a9c8e9508d89a53cfb18afdd8c358c7aa24e47359fda9841d7f89839b8a6b  height=105  log2_work=7.7279205  tx=106  date=2015-03-14 08:38:38 progress=1.000000  cache=105
2015-03-14 08:38:39 UpdateTip: new best=26b2e80af7c55b58e8eba6a5a1d68c53d8b634af5a4518196eea8ee762ab6c2c  height=106  log2_work=7.741467  tx=107  date=2015-03-14 08:38:38 progress=1.000000  cache=106
2015-03-14 08:38:39 UpdateTip: new best=02db35082dde7eb0e1aaf899f5e886d1feeefb9ca3045d3acc674df6835d63e9  height=107  log2_work=7.7548875  tx=108  date=2015-03-14 08:38:38 progress=1.000000  cache=107
2015-03-14 08:38:39 UpdateTip: new best=6e915443b9ac56f83fa91b720730315cf1ee2e1d148b74ad297027d05048a223  height=108  log2_work=7.7681843  tx=109  date=2015-03-14 08:38:39 progress=1.000000  cache=108
2015-03-14 08:38:39 UpdateTip: new best=2bd8f8431ab4fc27b6d5f0504461c2f4a1b7ea47cbaf69bd919f5c60c8add753  height=109  log2_work=7.7813597  tx=110  date=2015-03-14 08:38:39 progress=1.000000  cache=109
2015-03-14 08:38:39 UpdateTip: new best=078f2a8d3aa909247392cbd571ad753ef47f500bf5536a2bbfefce68ba168824  height=110  log2_work=7.7944159  tx=111  date=2015-03-14 08:38:39 progress=1.000000  cache=110
2015-03-14 08:38:39 UpdateTip: new best=71c9bad23f1909318b7d388d099eafa6eab1594750ebda37b10eb2f74f3e0455  height=111  log2_work=7.8073549  tx=112  date=2015-03-14 08:38:39 progress=1.000000  cache=111
2015-03-14 08:45:53 ResendWalletTransactions()

```

bitcore nodejs test
```
$ dc build
$ dc up -d
Recreating regdocker_seed1_1...
Recreating regdocker_seed2_1...
Recreating regdocker_bob_1...
Recreating regdocker_nred_1...
Recreating regdocker_alice_1...
$ nredsh

root@344a647c35d6:/myapp# ls
node_modules  regtest.js
root@344a647c35d6:/myapp# node regtest.js
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
cPvKW76ULG12sow54sQb21VJ7PyLqYNVVqeuuByc7aQahtjPt5w7
<Address: muJXdM1gQ8sighjFxQbQHsZwpr5kFNeSNt, type: pubkeyhash, network: regnet>
```

Fri Mar 13 15:20:26 CST 2015

```
$ source alias.sh
$ dc build
$ dc up -d
Creating regdocker_seed1_1...
Creating regdocker_seed2_1...
Creating regdocker_alice_1...
Creating regdocker_bob_1...
$ docker-compose ps
      Name               Command        State          Ports
--------------------------------------------------------------------
regdocker_alice_1   bitcoind -regtest   Up      18332/tcp, 18444/tcp
regdocker_bob_1     bitcoind -regtest   Up      18332/tcp, 18444/tcp
regdocker_seed1_1   bitcoind -regtest   Up      18332/tcp, 18444/tcp
regdocker_seed2_1   bitcoind -regtest   Up      18332/tcp, 18444/tcp

$ alicesh
root@55533a119406:/# cat /etc/hosts
172.17.0.31     55533a119406
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.17.0.30     seed2_1
172.17.0.29     regdocker_seed1_1
172.17.0.30     regdocker_seed2_1
172.17.0.29     seed1
172.17.0.29     seed1_1
172.17.0.30     seed2

root@55533a119406:/# rt getpeerinfo
[
    {
        "id" : 1,
        "addr" : "172.17.0.29:18444",
        "services" : "0000000000000001",
        "lastsend" : 1426231675,
        "lastrecv" : 1426231675,
        "bytessent" : 356,
        "bytesrecv" : 332,
        "conntime" : 1426231675,
        "pingtime" : 0.00353700,
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
        "addr" : "172.17.0.30:18444",
        "services" : "0000000000000001",
        "lastsend" : 1426231676,
        "lastrecv" : 1426231676,
        "bytessent" : 263,
        "bytesrecv" : 307,
        "conntime" : 1426231676,
        "pingtime" : 0.03791300,
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

root@55533a119406:/# rt setgenerate true 101
root@55533a119406:/# rt getbalance
50.00000000

exit

$ bobsh

root@ede089115365:/# rt getinfo
{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 0.00000000,
    "blocks" : 101,
    "timeoffset" : 0,
    "connections" : 2,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1426231676,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}

root@ede089115365:/# rt getnewaddress
msMS14b2PSDWsgDoVU7GdMVR1w6wvDbuGV

exit

$ alicesh

root@55533a119406:/# rt getbalance
50.00000000
root@55533a119406:/# rt sendtoaddress msMS14b2PSDWsgDoVU7GdMVR1w6wvDbuGV 38
f31dd12cfa730403e1b0dc3af51c1418db36a8013b5bbd98aa15532d00e2a188
root@55533a119406:/# rt getbalance
11.99999808
root@55533a119406:/# rt setgenerate true 6
[
    "4cb728f1ae2b60ce7082857f6c18ee36bb7bfd496df35bb0d98f1a60395b85fc",
    "6b46b487f35ded1b1b1ab9d241130a72ed6e5e6cba880ba3b4b4c9475bbaf27a",
    "47f54b7eae9b59f035ba3af2457452a706160ce348580b2f8a8b75d7059e5253",
    "1255fe51c240a6c6cb48e2aae28e05b75ed155285c66df8c391cc9dac9c78bab",
    "11ac7f18b16f78d622ea0347d7a62c834183d95d065aa729fab5fae0028a1657",
    "4e095c6ecd7a8e308216ac5fa7729c8d5a09f31d73e2e6e51a1cb4b520bd7e9b"
]
root@55533a119406:/# rt getbalance
311.99999808

exit

$ bobsh

root@ede089115365:/# rt getinfo
{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 38.00000000,
    "blocks" : 107,
    "timeoffset" : 0,
    "connections" : 2,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1426231676,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}

```


Fri Mar 13 14:52:37 CST 2015

one seed entry in docker-compose.yml with scale seed=2.cat /etc/hosts only one host_ip.

```
$ docker-compose build
$ docker-compose up -d
Creating regdocker_seed_1...
Creating regdocker_bob_1...
Creating regdocker_alice_1...

$ docker-compose scale seed=2
Creating regdocker_seed_2...
Starting regdocker_seed_2...

$ docker-compose ps
      Name               Command        State          Ports
--------------------------------------------------------------------
regdocker_alice_1   bitcoind -regtest   Up      18332/tcp, 18444/tcp
regdocker_bob_1     bitcoind -regtest   Up      18332/tcp, 18444/tcp
regdocker_seed_1    bitcoind -regtest   Up      18332/tcp, 18444/tcp
regdocker_seed_2    bitcoind -regtest   Up      18332/tcp, 18444/tcp

$ alias alicesh='docker exec -i -t regdocker_alice_1 bash'
$ alias bobsh='docker exec -i -t regdocker_bob_1 bash'

$ alicesh
root@7ba0cafb501a:/# cat /etc/hosts
172.17.0.25     7ba0cafb501a
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.17.0.23     regdocker_seed_1
172.17.0.23     seed
172.17.0.23     seed_1
```

Thu Mar 12 18:07:28 CST 2015

```
$ sudo pip install -U docker-compose
$ docker-compose --version
docker-compose 1.1.0
$ docker-compose build
$ docker-compose up -d
```

exec alice

```
$ docker exec -i -t regdocker_alice_1 bash

root@13328d7e0041:/# rt getinfo
{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 0.00000000,
    "blocks" : 0,
    "timeoffset" : 0,
    "connections" : 0,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1426159676,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}

root@13328d7e0041:/# rt getpeerinfo
[
]

root@13328d7e0041:/# rt getblockhash 0
0f9188f13cb7b2c71f2a335e3a4fc328bf5beb436012afca590b1a11466e2206

root@9f110a4fcc76:/# cat /etc/hosts
172.17.0.112    9f110a4fcc76
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.17.0.110    bob
172.17.0.110    bob_1
172.17.0.110    regdocker_bob_1

root@9f110a4fcc76:/# ping bob
PING bob (172.17.0.110) 56(84) bytes of data.
64 bytes from bob (172.17.0.110): icmp_seq=1 ttl=64 time=0.060 ms

root@9f110a4fcc76:/# rt addnode bob onetry
root@9f110a4fcc76:/# rt getpeerinfo
[
    {
        "id" : 1,
        "addr" : "bob",
        "services" : "0000000000000001",
        "lastsend" : 1426160386,
        "lastrecv" : 1426160386,
        "bytessent" : 356,
        "bytesrecv" : 332,
        "conntime" : 1426160386,
        "pingtime" : 0.10000900,
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


root@9f110a4fcc76:/# rt setgenerate true 101
[
    "2bc624c0ddaae65543b4f348b50a11e230cc05dca2c5b1a35c7b72466a21e8a3",
    "10525883132d4aee19bb1d1cc59df4590b458e859d0d65d2f7bb7b2eba09877d",
    "3bc832f411d8c0e649ed00d94651fe378908fe1376876fc6c8299406d0a44aee",

    "513832161749598ae05f7f08692ae7d4cb2b68aabdf31a6712b1a8eaeee2743d",
    "5c5a046c0b8f2a0b59c3ec70ef0f8556db479fc0ec7e7d29fd2c4271a2047ba3"
]

root@9f110a4fcc76:/# rt getbalance
50.00000000

root@9f110a4fcc76:/# rt sendtoaddress mgsVezXo8fcBbBdcbbgKQXFCdAmv4XLusg 42
fc60e58b570adebc12372cad85ef8eb953fe11727b038ca0264d21c6fbc7efab

root@9f110a4fcc76:/# rt getbalance
7.99999809
root@9f110a4fcc76:/# rt setgenerate true 6
[
    "2abba601bbb08b14476461028686c6ef193d6319b44d3e51c1374dfe2ebb0c34",
    "7aa72d2eca0b37b801348cef0de8ff947b583b8a778411fd9c6de51720a1252c",
    "245d4b36ef058503bd9fbdf0f549fed84cdb6e7ae1896cdefca12d27cbe5c540",
    "4ac89bcbbb0eb36a17627f25ce4a4982a8fe06b0eecfa34af71dc07a30f06124",
    "7acb8b11b9375dbab9539f11bd3002ff019cf6ce86583ab5c3c28e703b0db726",
    "4b23a2526c57a8547da6139bdd7ca8371faac050c1489af827a6b7ca60bf9550"
]
root@9f110a4fcc76:/# rt getbalance
307.99999809


```

exec bob

```
$ docker exec -i -t regdocker_bob_1 bash
root@602cc484e9b3:/# rt getinfo
{
    "version" : 100000,
    "protocolversion" : 70002,
    "walletversion" : 60000,
    "balance" : 0.00000000,
    "blocks" : 101,
    "timeoffset" : 0,
    "connections" : 1,
    "proxy" : "",
    "difficulty" : 0.00000000,
    "testnet" : false,
    "keypoololdest" : 1426159929,
    "keypoolsize" : 101,
    "paytxfee" : 0.00000000,
    "relayfee" : 0.00001000,
    "errors" : ""
}
root@602cc484e9b3:/# rt getpeerinfo
[
    {
        "id" : 1,
        "addr" : "172.17.0.112:50735",
        "services" : "0000000000000001",
        "lastsend" : 1426161106,
        "lastrecv" : 1426161106,
        "bytessent" : 16270,
        "bytesrecv" : 445452,
        "conntime" : 1426160386,
        "pingtime" : 0.10022900,
        "version" : 70002,
        "subver" : "/Satoshi:0.10.0/",
        "inbound" : true,
        "startingheight" : 0,
        "banscore" : 0,
        "synced_headers" : 101,
        "synced_blocks" : 101,
        "inflight" : [
        ],
        "whitelisted" : false
    }
]

root@602cc484e9b3:/# rt getnewaddress
mgsVezXo8fcBbBdcbbgKQXFCdAmv4XLusg

# pass to alice and send 42 btc
root@602cc484e9b3:/# rt getbalance
42.00000000

```
