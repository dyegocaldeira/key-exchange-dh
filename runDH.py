#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dh import DH
from prime import Prime

if __name__ == '__main__':

    message = "Mensagem secreta?!"

    c_private = 199
    j_private = 157

    prime = Prime()
    prime.createPrimeNumbers()

    print('[+] Public key 1: ' + str(prime.publicKey1))
    print('[+] Public key 2: ' + str(prime.publicKey2))

    Sadat = DH(c_private, prime.publicKey1, prime.publicKey2)
    Michael = DH(j_private, prime.publicKey1, prime.publicKey2)

    partial_key_sadat = Sadat.generatePartialKey()
    partial_key_michael = Michael.generatePartialKey()

    print('[+] partial key Carlos: ' + str(partial_key_sadat))
    print('[+] partial key Jose: ' + str(partial_key_michael))

    full_key_sadat = Sadat.generateFullKey(partial_key_michael)
    full_key_michael = Michael.generateFullKey(partial_key_sadat)
    
    print('[+] key Carlos: ' + str(full_key_sadat))
    print('[+] key Jose: ' + str(full_key_michael))

    print('[+] Mensagem enviada por Carlos: ' + message)
    print('[+] Mensagem recebida por José encriptada por Carlos: ' + Sadat.encryptMessage(message))

    msg_encrypted = Sadat.encryptMessage(message)
    print('[+] Mensagem recebida decriptada por Jose: ' + Michael.decryptMessage(msg_encrypted))
