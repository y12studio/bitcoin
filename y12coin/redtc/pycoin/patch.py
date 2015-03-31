#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import yaml

p = open('pycoin/pycoin/networks.py','r').read()
doc = yaml.load(open('pycoin.yml', 'r'))
for k in doc:
    p = p.replace(k,str(doc[k]))
p2 = open("pycoin/pycoin/networks.py", "wb")
p2.write(p)
p2.close()
