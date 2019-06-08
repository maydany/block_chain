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

