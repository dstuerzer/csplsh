

import hashlib as hl
import string as st
import random as rd
import time


def transactions(L):
    #generates random 'transaction text' for the current block
    return  ''.join([rd.choice(st.ascii_letters) for n in range(L)])

def hash_block(block):
    return hl.sha256(bytes(block[0]+block[1]+block[2], 'utf-8')).hexdigest()[:10]
#
#def check_chain(block_chain):
#    for i in range(1,len(block_chain)):
#        print(block_chain[i][0], sha_block(block_chain[i-1]))
#
#def localize_error(block_chain, L):
#    i = 1
#    while (i<len(block_chain)) and  (sha_block(block_chain[i-1])[:L] != '0' *L):
#        i += 1
#    return i
#
#def repair_chain(block_chain, L):
#    i = localize_error(block_chain, L)
#    while (i < len(block_chain)):
#        block_chain[i][2] = find_nounce(block_chain[i], L)
#        i = localize_error(block_chain, L)
#    return block_chain
#    
def find_nounce(block, difficulty):
    #completes the block (by a nounce) until the hash has at least 'difficulty' leading zeros
    j = 0
    block[2] = str(j)
    while hash_block(block)[:difficulty] != '0'*difficulty:
        j += 1
        block[2] = str(j)
    return str(j)
    
def generate_chain(length, difficulty):
    block_chain = [['prev. hash', 'transactions', 'nounce']] #structure of blocks
    block_chain[0][2] = find_nounce(block_chain[0], difficulty)
    length_chain = 10
    
    for i in range(1,length_chain):
        block = ['','','']
        block[0] = hash_block(block_chain[i-1])
        block[1] = 'transactions: '+transactions(5)  #random transaction text
        # MINING:
        block[2] = find_nounce(block, difficulty)
        #mining is complete, appropriate nounce found, hash starts with 'difficulty' zeros
        block_chain.append(block)
        
    return block_chain

def print_chain(block_chain):
    for block in block_chain:
        print(block)
    print("\n")
    
def check_chain(block_chain):
    for i in range(len(block_chain)-1):
        if hash_block(block_chain[i]) != block_chain[i+1][0]:
            #print("Block {} has been tampered with\n".format(i))
            return i
    #print("Block Chain is in order\n")
    return -1
        

def repair_chain(block_chain, difficulty):
    #repairs a broken chain (i.e. this is what a fraudster would have to do)
    i = check_chain(block_chain)
    while (i!=-1):
        block = block_chain[i]
        block[2] = find_nounce(block, difficulty)
        block_chain[i+1][0] = hash_block(block)
        print("repaired block {}".format(i))
        i = check_chain(block_chain)
    return block_chain

# INIT: Set difficulty, and generate the chain:

difficulty = 3
block_chain = generate_chain(10, difficulty)
print_chain(block_chain)

if check_chain(block_chain) == -1:
    print("chain is in order\n")
else:
    print("Block {} has been tampered with\n".format(check_chain(block_chain)))

# mess with a past block:

block_chain[4][1] = 'FRAUD!'
print_chain(block_chain)
if check_chain(block_chain) == -1:
    print("chain is in order\n")
else:
    print("Block {} has been tampered with\n".format(check_chain(block_chain)))

# Now generate a new, repaired chain:
block_chain_repaired = repair_chain(block_chain, difficulty)

print_chain(block_chain_repaired)
if check_chain(block_chain) == -1:
    print("chain is in order")
else:
    print("Block {} has been tampered with".format(check_chain(block_chain)))
