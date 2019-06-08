# Create a plain block chain
 
#Requirements
#Flask==0.12.2

#the libraries import
import datetime
import hashlib
import json
from flask import Flask, jsonify

#BUILD BLOCK CHAIN

class BlockChain:
    
    def __init__(self):
        self.chain = []
        self.create_block(nounce = 1, prev_hash = '0')

    def create_block(self, nounce, prev_hash):
        block = {'index': len(self.chain) + 1, 
                 'timestamp': str(datetime.datetime.now()),
                 'nounce': nounce,
                 'prev_hash': prev_hash}
        self.chain.append(block)
        return block
    
    def get_prev_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, prev_nounce):
        new_nounce = 1
        check_nounce = False
        while check_nounce is False:
            hash_operation = hashlib.sha256(str(new_nounce**2 - prev_nounce**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_nounce = True
            else:
                new_nounce += 1
        return new_nounce