var bitcore = require('bitcore');
var Networks = bitcore.Networks;
Networks.add({
  name: 'YP_COIN',
  alias: 'YP_COIN',
  pubkeyhash: 0xYP_HEX_PUBKEY_ADDRESS,
  privatekey: 0xYP_HEX_SECRET_KEY,
  scripthash: 0xYP_HEX_SCRIPT_ADDRESS,
  xpubkey: 0xYP_HEX_EXT_PUBLIC_KEY,
  xprivkey: 0xYP_HEX_EXT_SECRET_KEY,
  networkMagic: 0xfabfb5da,
  port: 18333,
  dnsSeeds: [
  ],
});
module.exports = {
  coinnet: Networks.get('YP_COIN')
};
