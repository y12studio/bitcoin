var coin = require('./coin');
var bitcore = require('bitcore');
var Mnemonic = require('bitcore-mnemonic');
var Address = bitcore.Address;

var net = coin.coinnet;
console.log(net);
var privateKey = bitcore.PrivateKey.fromRandom(net);
var wif = privateKey.toWIF();
var pubkey = privateKey.toPublicKey();
var addr = new Address(pubkey, net);
var r = {
    'wif': wif,
    'address': addr.toString(),
    'pubkey': pubkey.toString(),
    'privkey': privateKey.toString()
}
console.log(r);
var mnemonic = new Mnemonic();
var xprivkey = mnemonic.toHDPrivateKey('pass', net);
var xpubkey = xprivkey.hdPublicKey;
var m0h = xprivkey.derive("m/0'");
var m0h099 = xprivkey.derive("m/0'/0/99");
var m0h199 = xprivkey.derive("m/0'/1/99");
var hd = {
    'mnemonic': mnemonic.toString(),
    'xprivkey': xprivkey.toString(),
    'xpubkey': xpubkey.toString(),
    'ext/m/0h/0/99': {
        'priv': m0h099.toString(),
        'pub': m0h099.hdPublicKey.toString(),
        'addr': new Address(m0h099.hdPublicKey.publicKey, net).toString()
    },
    'int/m/0h/1/99': {
        'priv': m0h199.toString(),
        'pub': m0h199.hdPublicKey.toString(),
        'addr': new Address(m0h199.hdPublicKey.publicKey, net).toString()
    },
}
console.log(hd)
