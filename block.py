import hashlib
import time
import datetime

def calculate_hash(* args):
    return hashlib.sha256(" ".join([str(arg) for arg in args if arg is not None])).hexdigest()

class Block(object):
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    @classmethod
    def get_genesis_block(cls):
        return cls(0, "0", 1497922681, "Hello World", "e08ce3fe726b7ff79449d358e0b1019f088301152eddc89d8e4f9facdc6d0a9b");

    def short_timestamp(self):
        return datetime.datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def calculated_hash(self):
        return calculate_hash(self.index, self.previous_hash, self.timestamp, self.data)

    def is_valid(self):
        if self.hash != self.calculated_hash():
            return False
        return True

    @classmethod
    def generate_block(cls, previous_block, block_data=None):
        next_index = previous_block.index + 1
        next_timestamp = int(time.time())
        next_hash = calculate_hash(next_index, previous_block.hash, next_timestamp, block_data)
        return cls(next_index, previous_block.hash, next_timestamp, block_data, next_hash)

