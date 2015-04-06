#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,json,time
import nose.tools as nt
from requests.auth import HTTPBasicAuth

class TestWebRequest:

    @classmethod
    def setUpClass(cls):
        time.sleep(3)

    def rpctest(self,host):
        r = requests.get('http://%s:12332/'%host)
        # Unauthorized 401
        nt.eq_(401, r.status_code)
        data = '{"jsonrpc": "1.0", "id":"nosetest", "method": "getinfo", "params": [] }'
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post('http://%s:12332/'%host, data=data, headers=headers,auth=HTTPBasicAuth('user', 'pass'))
        nt.eq_(200, r.status_code)
        rj = r.json()['result']
        return rj

    def test_alice(self):
        rj = self.rpctest('alice')
        nt.eq_(0.0,rj['balance'])

    def test_bob(self):
        rj = self.rpctest('bob')
        nt.eq_(0.0,rj['balance'])

    def test_seeda(self):
        rj = self.rpctest('seeda')
        # balance keyerror by disablewallet
