#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:38:10 2018

@author: dominik
"""

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

from time import time

e = 2561737     # exponent
n = 5043197     # module

while True:
    prev_hash = input("Prev. hash:    ")
    transaction = input("Transaction: ")
    
    block = prev_hash+transaction
    print("\nThe block is:   " + prev_hash + '|' + transaction +'|xx\n')
    
    nounce = -1
    
    while True:
        nounce += 1
        block_number = int(block+str(nounce))
        t = time()
        while (time()-t < 0.8):
            1
                                
        hash_block = pow(block_number, e, n)    # computing the hash
        print("Nounce: {0:d},  Hash: {1:d}".format(nounce, hash_block % 1000))

        if (hash_block % 1000)<100:
            break
    
    print("\nThe complete block is "+ prev_hash + '|' + transaction +'|'+str(nounce))
    input()
    print("_____________________")
