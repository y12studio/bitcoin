#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import yaml

p = open('patchfile.v1','r').read()
doc = yaml.load(open('coin.yml', 'r'))
for k in doc:
    #print k,doc[k]
    p = p.replace(k,str(doc[k]))
p2 = open("patchfile.v2", "wb")
p2.write(p)
p2.close()
