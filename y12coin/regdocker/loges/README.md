Mon Mar 16 17:49:51 CST 2015

```
$ dc up -d
$ logessh

root@02cfe435c27e:/loges# netstat -at
tcp6       0      0 [::]:8333               [::]:*                  LISTEN
tcp6       0      0 [::]:9200               [::]:*                  LISTEN
tcp6       0      0 [::]:9300               [::]:*                  LISTEN
tcp6       0      0 [::]:9301               [::]:*                  LISTEN
tcp6       0      0 6a73bb049db6:9300       6a73bb049db6:42485      ESTABLISHED
tcp6       0      0 6a73bb049db6:42492      6a73bb049db6:9300       ESTABLISHED
tcp6       0      0 6a73bb049db6:9300       6a73bb049db6:42482      ESTABLISHED
tcp6       0      0 6a73bb049db6:42512      6a73bb049db6:9300       ESTABLISHED

root@6a73bb049db6:/loges# curl http://localhost:9200/
{
  "status" : 200,
  "name" : "Pixie",
  "version" : {
    "number" : "1.1.1",
    "build_hash" : "f1585f096d3f3985e73456debdc1a0745f512bbc",
    "build_timestamp" : "2014-04-16T14:27:12Z",
    "build_snapshot" : false,
    "lucene_version" : "4.7"
  },
  "tagline" : "You Know, for Search"
}

```
