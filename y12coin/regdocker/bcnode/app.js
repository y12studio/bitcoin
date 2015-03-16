var bitcore = require('bitcore');
var Networks = bitcore.Networks;
//var network = new bitcore.Network();
Networks.add({
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
// var regnet = Networks.get('regnet');
