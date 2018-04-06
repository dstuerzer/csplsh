#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 11:24:20 2018

@author: dominik
"""

from random import randint
# public key:
e = 2561737
n = 5043197

# private key:
    
d = 3255481

N = 20  # 1/N is the chance of success

prev_hash = input("Prev. Hash (last 3 dig): ")
transaction = input("Transaction numbers: ")
#
#prev_hash = '023'
#transaction = str(randint(1000,9999))

block = prev_hash + ' '+transaction
print("the block is:           " + block+' xx')


i = 0
#sentence.replace(" ", "")
block_nounce = block  + ' '+ str(i)
block_num = int( block_nounce.replace(" ", ""))
while (pow(block_num, e , n) > n//N):
    i += 1
    block_nounce = block + ' '+ str(i)
    block_num = int( block_nounce.replace(" ", ""))
    
cont = input("Press ENTER to show result!\n" )
print("the completed block is:"+' '+block_nounce)

print("Hash of completed block: ", block_num % 1000 )