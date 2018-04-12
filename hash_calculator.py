#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:17:24 2018

@author: dominik
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 11:24:20 2018

@author: Dominik
"""

e = 2561737     # exponent
n = 5043197     # module

while True:
    prev_hash = input("Prev. hash:    ")
    transaction = input("Transaction: ")
    
    block = prev_hash+transaction
    print("\nThe block is:   " + prev_hash + '|' + transaction)
    
    block_number = int(block)
    hash_block = pow(block_number, e, n)    # computing the hash
    
    
    prev_hash = str(hash_block % 1000)
    print("\nThe block's hash is "+prev_hash)
    input()
    print("_____________________")
