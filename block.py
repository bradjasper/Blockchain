import logging
import datetime

import hashing

class Block(object):
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

        self.readable_timestamp = datetime.datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def calculate_hash(self):
        return hashing.calculate(self.index, self.previous_hash, self.timestamp, self.data)

    def is_valid_hash(self):
        return self.hash == self.calculate_hash()

    def is_valid_block(self, previous_block):
        if (previous_block.index + 1) != self.index:
            logging.error("Invalid index")
            return False
        elif previous_block.hash != self.previous_hash:
            logging.error("Invalid previous hash")
            return False
        elif not self.is_valid_hash():
            logging.error("Invalid hash, block hash %s should be %s" % (self.hash, self.calculate_hash()))
            return False
        return True

    @classmethod
    def get_genesis_block(cls):
        logging.debug("Generating the genesis block")
        return cls(0, "0", 1497922681, "Hello World", "e08ce3fe726b7ff79449d358e0b1019f088301152eddc89d8e4f9facdc6d0a9b");

