import time

import hashing
from block import Block

# TODO: PoW

def generate_block(previous_block, block_data=None):
    next_index = previous_block.index + 1
    next_timestamp = int(time.time())
    next_hash = hashing.calculate(next_index, previous_block.hash, next_timestamp, block_data)
    return Block(next_index, previous_block.hash, next_timestamp, block_data, next_hash)

