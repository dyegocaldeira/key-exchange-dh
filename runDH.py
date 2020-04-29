#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dh import DH
from prime import Prime
import random

if __name__ == '__main__':

    message = "Mensagem secreta?!"

    c_private = random.randrange(1, 2048)
    j_private = random.randrange(1, 2048)

    prime = Prime()
    prime.createPrimeNumbers()

    print('[+] Private Key Carlos: ' + str(c_private))
    print('[+] Private Key Jose: ' + str(j_private))

    print('[+] Public key 1: ' + str(prime.publicKey1))
    print('[+] Public key 2: ' + str(prime.publicKey2))

    Carlos = DH(c_private, prime.publicKey1, prime.publicKey2)
    Jose = DH(j_private, prime.publicKey1, prime.publicKey2)

    partial_key_carlos = Carlos.generatePartialKey()
    partial_key_jose = Jose.generatePartialKey()

    print('[+] partial key Carlos: ' + str(partial_key_carlos))
    print('[+] partial key Jose: ' + str(partial_key_jose))

    Carlos.generateFullKey(partial_key_jose)
    Jose.generateFullKey(partial_key_carlos)
    
    print('[+] key Carlos: ' + str(Carlos.fullKey))
    print('[+] key Jose: ' + str(Jose.fullKey))

    print('[+] Mensagem enviada por Carlos: ' + message)
    print('[+] Mensagem recebida por José encriptada por Carlos: ' + Carlos.encryptMessage(message))

    msg_encrypted = Carlos.encryptMessage(message)
    print('[+] Mensagem recebida decriptada por Jose: ' + Jose.decryptMessage(msg_encrypted))
