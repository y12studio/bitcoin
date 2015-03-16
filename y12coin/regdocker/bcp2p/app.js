// bitcore-p2p/bitcoind.js at master · bitpay/bitcore-p2p
// https://github.com/bitpay/bitcore-p2p/blob/master/integration/bitcoind.js
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
  port: 18332,
  dnsSeeds: [
  ],
});

var regnet = Networks.get('regnet');
var bcp2p = require('bitcore-p2p');
var Peer = bcp2p.Peer;
var Messages = bcp2p.Messages;

linkhost = process.env.LINK_HOST;

var peer = new Peer(linkhost,18444,regnet);

peer.on('ready', function() {
  // peer info
  console.log(peer.version, peer.subversion, peer.bestHeight);
});
peer.on('disconnect', function() {
  console.log('connection closed');
});

peer.once('block', function(message) {
    console.log(message);
});
// handle events
peer.on('inv', function(msg) {
  // message.inventory[]
  console.log(msg);
  var message = new Messages.GetData(msg.inventory);
  peer.sendMessage(message);
});

peer.on('tx', function(message) {
  // message.transaction
  console.log(message)
});

peer.connect();
