#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '4ido10n'
from M2Crypto import RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode
flag = open('level1.passwd.enc','r').read()
key = open('private1.pem', "r").read()
rsakey = RSA.importKey(key)
rsakey = PKCS1_OAEP.new(rsakey)
decrypted = rsakey.decrypt(b64decode(flag))
print decrypted