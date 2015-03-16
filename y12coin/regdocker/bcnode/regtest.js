var bitcore = require('bitcore');
//var network = new bitcore.Network();
bitcore.Networks.add({
  name: 'regnet',
  alias: 'regnet',
  pubkeyhash: 0x6f,
  privatekey: 0xef,
  scripthash: 0xc4,
  xpubkey: 0x043587cf,
  xprivkey: 0x04358394,
  networkMagic: 0xfabfb5da,
  port: 18333,
  dnsSeeds: [
  ],
});
var regnet = bitcore.Networks.get('regnet');
console.log(regnet);
var privateKey = bitcore.PrivateKey.fromRandom(regnet);
var wif = privateKey.toWIF();
var pubkey = privateKey.toPublicKey();
var addr = new bitcore.Address(pubkey, regnet);
console.log(wif);
console.log(addr);
