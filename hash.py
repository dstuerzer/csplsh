#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 11:24:20 2018

@author: Dominik
"""

e = 2561737     # exponent
n = 5043197     # module

N = 10  # 1:N is the chance of success

prev_hash = '000'     # setting the initial hash

while True:
    transaction = input("Transaction numbers: ")
    block = prev_hash+transaction
    print("\nThe new block is:           " + prev_hash + ' ' + transaction +' xx')
    
    while True:
        nounce = input("Guess the nounce: ")
        block_number = int(block+nounce)
        hash_block = pow(block_number, e, n)    # computing the hash
        if hash_block < n/N:
            print("CORRECT! The completed block is " + prev_hash + ' ' + transaction +' '+nounce)
            input("")
            break
    
    prev_hash = str(hash_block % 1000)
    print("#####################\nMINING THE NEXT BLOCK!\n\nPrevious hash is "+prev_hash)
