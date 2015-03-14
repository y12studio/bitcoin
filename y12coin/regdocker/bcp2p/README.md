```
$ dc up -d
Recreating bitreg_seeda_1...
Recreating bitreg_seedb_1...
Recreating bitreg_bob_1...
Recreating bitreg_nred_1...
Recreating bitreg_alice_1...
Recreating bitreg_bcp2p_1...
Recreating bitreg_bitcoind_1...

$ bcp2psh
root@a0764a8d4449:/bcp2p# ls
app.js  node_modules
root@a0764a8d4449:/bcp2p# node app.js
70002 '/Satoshi:0.10.0/' 101

# after bobsh# rt setgenerate true 10
{ command: 'inv',
  inventory:
   [ { type: 2,
       typeName: 'BLOCK',
       hash: <Buffer 21 be ca 76 73 a5 fa c8 7d ff a6 09 25 84 3f 61 a1 d1 50 62 92 74 82 46 72 bf 3d c3 70 cf 4f 01> } ] }
{ command: 'inv',
  inventory:
   [ { type: 2,
       typeName: 'BLOCK',
       hash: <Buffer be 38 fd d0 4e 48 5d 72 1a d4 08 79 92 05 03 c5 ee 6e bf e9 11 7c 53 1c b5 a7 4b 1c b5 2f 87 40> } ] }
{ command: 'inv',
  inventory:
   [ { type: 2,
       typeName: 'BLOCK',
       hash: <Buffer 0d 61 56 0d 81 78 2e 08 bf ee cf f4 5f 9a a1 fd 49 82 6e 8e 9e c6 9a 32 05 0a 7f 04 2e d4 0b 71> } ] }
{ command: 'inv',
  inventory:
   [ { type: 2,
       typeName: 'BLOCK',
       hash: <Buffer e4 b0 10 61 24 37 74 22 ac 9f 34 88 3e 75 fc 95 d7 4e 79 d7 5b 4d 2f ca e1 c6 94 d9 44 41 1f 30> } ] }
{ command: 'inv',
  inventory:
   [ { type: 2,
       typeName: 'BLOCK',
       hash: <Buffer 51 aa 2e 8d 66 ec ee 19 16 8c b3 aa 27 c9 df eb 02 96 cd d4 8f 5e 0d d3 0d 2f b8 eb 02 a3 00 4e> } ] }
{ command: 'inv',
  inventory:
   [ { type: 2,
       typeName: 'BLOCK',
       hash: <Buffer 8f 77 c0 0c 51 da 93 ee 79 f6 e3 58 e0 43 c7 86 54 1d 06 eb ed ce 2f c8 d1 cb 67 48 86 b8 27 6b> } ] }
{ command: 'inv',
  inventory:
   [ { type: 2,
       typeName: 'BLOCK',
       hash: <Buffer 49 88 e1 7f b8 d2 6a 92 72 99 9e 7a f9 ce 88 1a ee b5 32 80 43 b6 ac bb c0 ca 95 d7 14 96 87 38> } ] }
{ command: 'inv',
  inventory:
   [ { type: 2,
       typeName: 'BLOCK',
       hash: <Buffer 6d ce cd 26 69 ef 53 8b ab 94 df c3 3c e1 ab b5 5d 6c b4 62 9c 85 9e 80 5e a2 fe 0e bd 13 fe 2a> } ] }
{ command: 'inv',
  inventory:
   [ { type: 2,
       typeName: 'BLOCK',
       hash: <Buffer 22 ca e6 43 82 6c 20 fa e5 b7 d6 c1 74 50 a6 21 6c ea e2 0c 98 56 f1 b2 23 5b 42 8a 28 df 68 74> } ] }
{ command: 'inv',
  inventory:
   [ { type: 2,
       typeName: 'BLOCK',
       hash: <Buffer 8a c6 7f f5 e8 ff 11 8b 94 e9 91 5d 7c 04 1b 9b 1c d2 8c 15 52 92 7b 19 b1 f3 b9 02 d2 45 1d 35> } ] }


# after bobsh# rt sendtoaddress msMS14b2PSDWsgDoVU7GdMVR1w6wvDbuGV 38
# Peer receives inv frame then sends a getdata frame back

{ command: 'inv',
  inventory:
   [ { type: 1,
       typeName: 'TX',
       hash: <Buffer ae 3c 72 ce 94 f7 94 6b 62 24 fd 6d 36 83 33 a5 e2 43 2a 4d 57 53 8e 94 56 be 46 c4 d7 b0 22 ee> } ] }

# getdata back

{ command: 'tx',
  transaction: <Transaction: 01000000018a9230c339d50ab94dbd8aeada607c13770398e60050821ec58b4e7c0f247c2500000000484730440220536376bfca7376bd4950ea868ddb01f3f2a821e47159e826046aca913213bcb802204a38a446d1399a7013ff0752b5b378547b1070e4cdf631dfb35934531990457001ffffffff0200667fe2000000001976a91481d47a7ca12cd69fe5ad18223e8992400881e77188ac418b8647000000001976a914e80fe659b768dd98b9d5d1daf42d8e2a4c36d99488ac00000000> }

```
