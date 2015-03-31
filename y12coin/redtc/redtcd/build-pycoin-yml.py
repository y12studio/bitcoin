#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import yaml

doc = yaml.load(open('coin.yml', 'r'))
r={}
r['ABC'] = 'abc'
r = {k:v for (k,v) in doc.iteritems() if 'YP_' in k}
#
#
# YP_HEX_SECRET_KEY: ff
# YP_HEX_PUBKEY_ADDRESS: ff
# YP_HEX_SCRIPT_ADDRESS: ff
r['YP_HEX_SECRET_KEY'] = format(doc['Y_B58_SECRET_KEY'],'x')
r['YP_HEX_PUBKEY_ADDRESS'] = format(doc['Y_B58_PUBKEY_ADDRESS'],'x')
r['YP_HEX_SCRIPT_ADDRESS'] = format(doc['Y_B58_SCRIPT_ADDRESS'],'x')
with open('../pycoin/pycoin.yml', 'wb') as f:
    yaml.dump(r, f,default_flow_style=False)

    #p = p.replace(k,str(doc[k]))
#p2 = open("patchfile.v2", "wb")
#p2.write(p)
#p2.close()
