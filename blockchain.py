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
        self.create_block(proof = 1, prev_hash = '0')

    def create_block(self, proof, prev_hash):
        block = {'index': len(self.chain) + 1, 
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'prev_hash': prev_hash}
        self.chain.append(block)
        return block
    
    def get_prev_block(self):
        return self.chain[-1]