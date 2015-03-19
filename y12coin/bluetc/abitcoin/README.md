Thu Mar 19 12:48:35 CST 2015

```
$ docker build -t y12docker/foo .

$ docker images | grep foo
y12docker/foo              latest              32fadb311316        7 minutes ago       28.74 MB

$ docker run y12docker/foo ldd /usr/bin/bitcoind
        /lib/ld-musl-x86_64.so.1 (0x7ff42a6fd000)
        libboost_system.so.1.57.0 => /usr/lib/libboost_system.so.1.57.0 (0x7ff42a057000)
        libboost_filesystem.so.1.57.0 => /usr/lib/libboost_filesystem.so.1.57.0 (0x7ff429e3e000)
        libboost_program_options-mt.so.1.57.0 => /usr/lib/libboost_program_options-mt.so.1.57.0 (0x7ff429bc5000)
        libboost_thread-mt.so.1.57.0 => /usr/lib/libboost_thread-mt.so.1.57.0 (0x7ff4299a0000)
        libdb_cxx-5.3.so => /usr/lib/libdb_cxx-5.3.so (0x7ff4295f3000)
        libssl.so.1.0.0 => /lib/libssl.so.1.0.0 (0x7ff42938d000)
        libcrypto.so.1.0.0 => /lib/libcrypto.so.1.0.0 (0x7ff428f72000)
        libstdc++.so.6 => /usr/lib/libstdc++.so.6 (0x7ff428c7f000)
        libgcc_s.so.1 => /usr/lib/libgcc_s.so.1 (0x7ff428a6d000)
        libc.musl-x86_64.so.1 => /lib/ld-musl-x86_64.so.1 (0x7ff42a6fd000)
        libboost_system-mt.so.1.57.0 => /usr/lib/libboost_system-mt.so.1.57.0 (0x7ff428869000)
        libboost_atomic-mt.so.1.57.0 => /usr/lib/libboost_atomic-mt.so.1.57.0 (0x7ff428667000)
        libz.so.1 => /lib/libz.so.1 (0x7ff428450000)

$ docker run y12docker/foo bitcoin-cli --version
        Bitcoin Core RPC client version v0.10.0.0-de31a22-dirty


$ docker run y12docker/foo bitcoind
        Error: To use bitcoind, or the -server option to bitcoin-qt, you must set an rpcpassword in the configuration file:
        /root/.bitcoin/bitcoin.conf
        It is recommended you use the following random password:
        rpcuser=bitcoinrpc
        rpcpassword=8puQ3oAf4efvgb9wrKyMsvwDEtoMFa9E8zkuwfGwnw1G
        (you do not need to remember this password)
        The username and password MUST NOT be the same.
        If the file does not exist, create it with owner-readable-only file permissions.
        It is also recommended to set alertnotify so you are notified of problems;
        for example: alertnotify=echo %s | mail -s "Bitcoin Alert" admin@foo.com

```
