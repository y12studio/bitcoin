NOTE: Outdated way.

Alpine is based on musl not glibc.

```
$ source alias.sh
$ bi
$ bb
$ readelf -d xbutcd/bin/bitcoind

Dynamic section at offset 0x458b88 contains 39 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libboost_system.so.1.54.0]
 0x0000000000000001 (NEEDED)             Shared library: [libboost_filesystem.so.1.54.0]
 0x0000000000000001 (NEEDED)             Shared library: [libboost_program_options.so.1.54.0]
 0x0000000000000001 (NEEDED)             Shared library: [libboost_thread.so.1.54.0]
 0x0000000000000001 (NEEDED)             Shared library: [libdb_cxx-5.1.so]
 0x0000000000000001 (NEEDED)             Shared library: [libssl.so.1.0.0]
 0x0000000000000001 (NEEDED)             Shared library: [libcrypto.so.1.0.0]
 0x0000000000000001 (NEEDED)             Shared library: [libanl.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libstdc++.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libm.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libgcc_s.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libpthread.so.0]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000000c (INIT)               0x23208


$ docker run y12docker/xbutcd ldd /usr/bin/vi
        /lib/ld-musl-x86_64.so.1 (0x7f73e5ac3000)
        libc.musl-x86_64.so.1 => /lib/ld-musl-x86_64.so.1 (0x7f73e5ac3000)
```
