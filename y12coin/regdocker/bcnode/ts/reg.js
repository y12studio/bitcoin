var bitcore = require('bitcore');
var regnet = bitcore.Networks.get('regnet');
var NetworkWrap = (function () {
    function NetworkWrap() {
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
        this.network = bitcore.Networks;
        this.regnet = this.network.get('regnet');
    }
    return NetworkWrap;
})();
var nw = new NetworkWrap();
console.log(nw.network);
console.log(nw.regnet);
var privateKey = bitcore.PrivateKey.fromRandom(regnet);
var wif = privateKey.toWIF();
var pubkey = privateKey.toPublicKey();
var addr = new bitcore.Address(pubkey, regnet);
console.log(wif);
console.log(addr);
