#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import yaml

p = open('coin.js.tpl','r').read()
doc = yaml.load(open('pycoin.yml', 'r'))
for k in doc:
    p = p.replace(k,str(doc[k]))
p2 = open("coin.js", "wb")
p2.write(p)
p2.close()
