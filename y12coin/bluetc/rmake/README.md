[aports/testing/bitcoin at master · alpinelinux/aports](https://github.com/alpinelinux/aports/tree/master/testing/bitcoin)

```
$ source alias.sh
$ dc build rbase
$ dc build rmake
$ rmakesh


bash-4.3# bitcoin-cli --version
Bitcoin Core RPC client version v0.10.0.0-g047a898
bash-4.3# ldd /usr/bin/bitcoin-cli
        /lib/ld-musl-x86_64.so.1 (0x7fc524bf4000)
        libboost_system.so.1.57.0 => /usr/lib/libboost_system.so.1.57.0 (0x7fc524779000)
        libboost_filesystem.so.1.57.0 => /usr/lib/libboost_filesystem.so.1.57.0 (0x7fc524560000)
        libboost_program_options-mt.so.1.57.0 => /usr/lib/libboost_program_options-mt.so.1.57.0 (0x7fc5242e7000)
        libboost_thread-mt.so.1.57.0 => /usr/lib/libboost_thread-mt.so.1.57.0 (0x7fc5240c2000)
        libboost_chrono-mt.so.1.57.0 => /usr/lib/libboost_chrono-mt.so.1.57.0 (0x7fc523eba000)
        libssl.so.1.0.0 => /lib/libssl.so.1.0.0 (0x7fc523c54000)
        libcrypto.so.1.0.0 => /lib/libcrypto.so.1.0.0 (0x7fc523839000)
        libstdc++.so.6 => /usr/lib/libstdc++.so.6 (0x7fc523546000)
        libgcc_s.so.1 => /usr/lib/libgcc_s.so.1 (0x7fc523334000)
        libc.musl-x86_64.so.1 => /lib/ld-musl-x86_64.so.1 (0x7fc524bf4000)
        libboost_system-mt.so.1.57.0 => /usr/lib/libboost_system-mt.so.1.57.0 (0x7fc523130000)
        libboost_atomic-mt.so.1.57.0 => /usr/lib/libboost_atomic-mt.so.1.57.0 (0x7fc522f2e000)
        libz.so.1 => /lib/libz.so.1 (0x7fc522d17000)

```
