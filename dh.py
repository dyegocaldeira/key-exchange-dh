#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simplecrypt import encrypt, decrypt

""" 
    Exemplo regras:

    privateKey = 18
    publicKey1 = 13
    publicKey2 = 5

    partialKey = (publicKey2 ^ privateKey) mod publicKey1
    partialKey = (5 ^ 18) mod 13
    partialKey = (5 ** 18) % 13
    myPartialKey = 12

    friendPartilKey = 8

    key = (friendPartilKey ^ privateKey) mod publicKey1
    key = (8 ^ 18) mod 13
    key = (8 ** 18) % 13
    key = 12
"""

class DH(object):

    def __init__(self, privateKey, publicKey1, publicKey2):

        self.publicKey1 = publicKey1
        self.publicKey2 = publicKey2
        self.privateKey = privateKey
        self.fullKey = None

    def generatePartialKey(self):

        partialKey = self.publicKey2**self.privateKey
        partialKey = partialKey % self.publicKey1

        return partialKey

    def generateFullKey(self, partialKey):

        fullKey = partialKey**self.privateKey
        fullKey = fullKey % self.publicKey1
        self.fullKey = fullKey

        return fullKey

    def encryptMessage(self, message):

        encryptedMessage = encrypt(str(self.fullKey), message)

        return encryptedMessage

    def decryptMessage(self, encryptedMessage):

        return decrypt(str(self.fullKey), encryptedMessage).decode('utf8')
