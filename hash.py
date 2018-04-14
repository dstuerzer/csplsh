#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 11:24:20 2018

@author: Dominik
"""
from time import time

def wait():
    t = time()
    while ((time()-t) < 0.5):
        1
        
e = 2561737     # exponent
n = 5043197     # module

N = 10  # 1:N is the chance of success

prev_hash = '000'     # setting the initial hash

while True:
    transaction = input("Transaction numbers: ")
    block = prev_hash+transaction
    print("\nThe new block is:           " + prev_hash + ' ' + transaction +' xx')
    
    while True:
        wait()
        nounce = input("\nGuess the nounce: ")
        wait()
        block_number = int(block+nounce)
        hash_block = pow(block_number, e, n) % 1000    # computing the hash
        if hash_block < 1000/N:
            print("         CORRECT!    Hash: {}\n         The completed block is ".format(hash_block) + prev_hash + ' ' + transaction +' '+nounce)
            input("")
            break
        else:
            print("         TRY AGAIN! Hash: {}".format(hash_block))
    
    prev_hash = str(hash_block % 1000)
    print("#####################\nMINING THE NEXT BLOCK!\n\nPrevious hash is "+prev_hash)
