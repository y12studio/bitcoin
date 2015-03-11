#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# fastcoin/genesis at fastcoin · imharrywu/fastcoin
# https://github.com/imharrywu/fastcoin/tree/fastcoin/genesis
# python genesis.py -z "TestTimeStamp" -p "040184710fa689ad5023690c80f3a49c8f13f8d45b8c857fbcbc8bc4a8e4d3eb4b10f4d4604fa08dce601aaf0f470216fe1b51850b4acf21b179c45070ac7b03a9" -t 1317972665 -n 2084524493
#
import hashlib, binascii, struct, array, os, time, sys, optparse
from construct import *

def main():
    options = get_args()
    print '==== options ===='
    print options
    algorithm = 'SHA256'
    # https://en.bitcoin.it/wiki/Difficulty
    #
    # scrypt or X11/X13/X15
    bits,target = 0x1e0ffff0, 0x0ffff0 * 2**(8*(0x1e - 3))
    # bitcoin
    # bits, target = 0x1d00ffff, 0x00ffff * 2**(8*(0x1d - 3))
    input_script  = create_input_script(options.timestamp)
    output_script = create_output_script(options.pubkey)
    tx = create_transaction(input_script, output_script,options)
    hash_merkle_root = hashlib.sha256(hashlib.sha256(tx).digest()).digest()
    print '\n==== block info ===='
    print_block_info(options, hash_merkle_root, bits)
    block_header = create_block_header(hash_merkle_root, options.time, bits, options.nonce)
    print '\n==== generate hash ===='
    genesis_hash, nonce = generate_hash(block_header, algorithm, options.nonce, target)
    print '\n==== genesis found ===='
    announce_found_genesis(genesis_hash, nonce)
    print '==== END ===='

def create_block_header(hash_merkle_root, time, bits, nonce):
    block_header = Struct("block_header",
      Bytes("version",4),
      Bytes("hash_prev_block", 32),
      Bytes("hash_merkle_root", 32),
      Bytes("time", 4),
      Bytes("bits", 4),
      Bytes("nonce", 4))

    genesisblock = block_header.parse('\x00'*80)
    genesisblock.version          = struct.pack('<I', 1)
    genesisblock.hash_prev_block  = struct.pack('<qqqq', 0,0,0,0)
    genesisblock.hash_merkle_root = hash_merkle_root
    genesisblock.time             = struct.pack('<I', time)
    genesisblock.bits             = struct.pack('<I', bits)
    genesisblock.nonce            = struct.pack('<I', nonce)
    return block_header.build(genesisblock)

# https://en.bitcoin.it/wiki/Block_hashing_algorithm
def generate_hash(data_block, algorithm, start_nonce, target):
    print 'Searching for genesis hash..'
    nonce           = start_nonce
    last_updated    = time.time()
    difficulty      = float(0xFFFF) * 2**208 / target
    update_interval = int(1000000 * difficulty)

    while True:
      sha256_hash, header_hash = generate_hashes_from_block(data_block, algorithm)
      last_updated = calculate_hashrate(nonce, update_interval, difficulty, last_updated)
      if is_genesis_hash(header_hash, target):
        if algorithm == "X11" or algorithm == "X13" or algorithm == "X15":
          return (header_hash, nonce)
        return (sha256_hash, nonce)
      else:
       nonce = nonce + 1
       data_block = data_block[0:len(data_block) - 4] + struct.pack('<I', nonce)

def generate_hashes_from_block(data_block, algorithm):
    sha256_hash = hashlib.sha256(hashlib.sha256(data_block).digest()).digest()[::-1]
    header_hash = ""
    if algorithm == 'scrypt':
      header_hash = scrypt.hash(data_block,data_block,1024,1,1,32)[::-1]
    elif algorithm == 'SHA256':
      header_hash = sha256_hash
    elif algorithm == 'X11':
      try:
        exec('import %s' % "xcoin_hash")
      except ImportError:
        sys.exit("Cannot run X11 algorithm: module xcoin_hash not found")
      header_hash = xcoin_hash.getPoWHash(data_block)[::-1]
    elif algorithm == 'X13':
      try:
        exec('import %s' % "x13_hash")
      except ImportError:
        sys.exit("Cannot run X13 algorithm: module x13_hash not found")
      header_hash = x13_hash.getPoWHash(data_block)[::-1]
    elif algorithm == 'X15':
      try:
        exec('import %s' % "x15_hash")
      except ImportError:
        sys.exit("Cannot run X15 algorithm: module x15_hash not found")
      header_hash = x15_hash.getPoWHash(data_block)[::-1]
    return sha256_hash, header_hash

def is_genesis_hash(header_hash, target):
    return int(header_hash.encode('hex_codec'), 16) < target


def calculate_hashrate(nonce, update_interval, difficulty, last_updated):
    if nonce % update_interval == update_interval - 1:
      now             = time.time()
      hashrate        = round(update_interval/(now - last_updated))
      generation_time = round(difficulty * pow(2, 32) / hashrate / 3600, 1)
      sys.stdout.write("\r%s hash/s, estimate: %s h"%(str(hashrate), str(generation_time)))
      sys.stdout.flush()
      return now
    else:
      return last_updated

def create_input_script(psz_timestamp):
    psz_prefix = ""
    #use OP_PUSHDATA1 if required
    if len(psz_timestamp) > 76: psz_prefix = '4c'

    script_prefix = '04ffff001d0104' + psz_prefix + chr(len(psz_timestamp)).encode('hex')
    print (script_prefix + psz_timestamp.encode('hex'))
    return (script_prefix + psz_timestamp.encode('hex')).decode('hex')


def create_output_script(pubkey):
    script_len = '41'
    OP_CHECKSIG = 'ac'
    return (script_len + pubkey + OP_CHECKSIG).decode('hex')

def print_block_info(options, hash_merkle_root, bits):
    #print "algorithm: "    + (options.algorithm)
    print "merkle hash: "  + hash_merkle_root[::-1].encode('hex_codec')
    print "pszTimestamp: " + options.timestamp
    print "pubkey: "       + options.pubkey
    print "time: "         + str(options.time)
    print "bits: "         + str(hex(bits))


def create_transaction(input_script, output_script,options):
    transaction = Struct("transaction",
      Bytes("version", 4),
      Byte("num_inputs"),
      StaticField("prev_output", 32),
      UBInt32('prev_out_idx'),
      Byte('input_script_len'),
      Bytes('input_script', len(input_script)),
      UBInt32('sequence'),
      Byte('num_outputs'),
      Bytes('out_value', 8),
      Byte('output_script_len'),
      Bytes('output_script',  0x43),
      UBInt32('locktime'))

    tx = transaction.parse('\x00'*(127 + len(input_script)))
    tx.version           = struct.pack('<I', 1)
    tx.num_inputs        = 1
    tx.prev_output       = struct.pack('<qqqq', 0,0,0,0)
    tx.prev_out_idx      = 0xFFFFFFFF
    tx.input_script_len  = len(input_script)
    tx.input_script      = input_script
    tx.sequence          = 0xFFFFFFFF
    tx.num_outputs       = 1
    tx.out_value         = struct.pack('<q' ,options.value)
    tx.output_script_len = 0x43
    tx.output_script     = output_script
    tx.locktime          = 0
    return transaction.build(tx)

def announce_found_genesis(genesis_hash, nonce):
    print "genesis hash found!"
    print "nonce: "        + str(nonce)
    print "genesis hash: " + genesis_hash.encode('hex_codec')

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--time", dest="time", default=int(time.time()),
                   type="int", help="the (unix) time when the genesisblock is created")
    parser.add_option("-z", "--timestamp", dest="timestamp", default="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks",
                   type="string", help="the pszTimestamp found in the coinbase of the genesisblock")
    parser.add_option("-n", "--nonce", dest="nonce", default=0,
                   type="int", help="the first value of the nonce that will be incremented when searching the genesis hash")
    parser.add_option("-p", "--pubkey", dest="pubkey", default="04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f",
                   type="string", help="the pubkey found in the output script")
    parser.add_option("-v", "--value", dest="value", default=5000000000,
                   type="int", help="the value in coins for the output, full value (exp. in bitcoin 5000000000 - To get other coins value: Block Value * 100000000)")

    (options, args) = parser.parse_args()
    return options

main()
