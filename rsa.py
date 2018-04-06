#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 10:24:21 2018

@author: dominik
"""
from numpy import random as rd
import numpy as np
from random import randint
from math import gcd



def isPrime(n, k=10): # miller-rabin

    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for i in range(k):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1: continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


low  = 1000
mid  = 2000
high = 3000


p = rd.randint(low, mid)
while (not isPrime(p)):
    p = rd.randint(low, mid)

q = rd.randint(mid, high)
while (not isPrime(q)):
    q = rd.randint(mid, high)
#
print(p,q)
n = p*q
print("n    =",n)
phi = (p-1)*(q-1)
print("phi  =", phi)

e = randint(phi//2, phi-1)
while (gcd(e,phi) != 1):
    e = randint(phi//2, phi-1)
    
print("e    =",e)

d = modinv(e,phi)

print("d    =",d)

print(d*e % phi)

m = randint(1,n-1)
#
#print("m    =",m)
#c = pow(m,e,n)  # this is the trapdoor
#print("c    =", c)
#print("m    =", pow(c,d,n))

print("public pair: n = {}, e = {}".format(n,e))
print("private key: d = {}".format(d))


