#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Prime(object):

    def __init__(self):

        self.publicKey1 = None
        self.publicKey2 = None

    def createPrimeNumbers(self):

        for i in range(1, 3):

            isPrime = False
            randStart = 32 if i == 1 else 1
            randFinish = 2048 if i == 1 else 31

            while isPrime == False:

                public = random.randrange(randStart, randFinish)
                isPrime = self.validatePrimeNumber(public)

                if isPrime and i == 1:
                    self.publicKey1 = public

                if isPrime and i == 2:
                    self.publicKey2 = public

    def validatePrimeNumber(self, n):

        for i in range(2, 7):
            if ((i**(n-1)) % n) != 1:
                return False

        return True
