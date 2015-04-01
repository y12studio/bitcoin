var coin = require('./coin');
var Mnemonic = require('bitcore-mnemonic');
var net = coin.coinnet;
console.log(net);
var mnemonic = new Mnemonic();
var xprivkey = mnemonic.toHDPrivateKey('pass',net);
console.log(mnemonic.toString())
console.log(xprivkey)
