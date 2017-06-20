import hashlib
import time
import json
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

class Blockchain(object):

    def __init__(self):
        print("Welcome to blockchain")
        self.blockchain = [Block.get_genesis_block()]
        self.stats()

    def last_block(self):
        return self.blockchain[-1]

    def generate_next_block(self, block_data=None):
        next_block = Block.generate_block(self.last_block(), block_data)
        self.blockchain.append(next_block)

    def is_valid_new_block(self, new_block, previous_block):
        if (previous_block.index + 1) != new_block.index:
            self.error("Invalid index")
            return False
        elif previous_block.hash != new_block.previous_hash:
            self.error("Invalid previous hash")
            return False
        elif not new_block.is_valid():
            self.error("Invalid hash, block hash %s should be %s" % (new_block.hash, new_block.calculated_hash()))
            return False

    def stats(self):
        print("There are %d blocks in the blockchain" % len(self.blockchain))
        for block in self.blockchain:
            if not block.is_valid():
                self.error("Invalid hash, block hash %s should be %s" % (block.hash, block.calculated_hash()))
                assert False, "Blockchain failed integrity test"
            print("%d\t%s\t%s\t%s" % (block.index, block.short_timestamp(), block.hash, block.data))

    def is_valid_chain(self, new_blocks):
        for i, block in enumerate(new_blocks):
            if i == 0:
                if (json.dumps(block) != json.dumps(self.blockchain[i])):
                    self.error("Genesis blocks are not the same")
                    return False
            elif not self.is_valid_new_block(block, new_blocks[i-1]):
                    return False

        return True

    def replace_chain(self, new_blocks):
        if self.is_valid_chain(new_blocks) and len(new_blocks) > len(self.blockchain):
            print("Received new valid blockchain, replacing...");
            self.blockchain = new_blocks
            self.broadcast(self.last_response_message())
        else:
            self.error("Received invalid blockchain");

    def error(self, msg):
        print("ERROR: %s" % msg)

    def broadcast(self):
        print("Notifying peers");
        # TODO: Implement

    def last_response_message(self):
        pass
        # TODO: Create message for last block mined

blockchain = Blockchain()

for i in range(1000):
    blockchain.generate_next_block("block data = %d" % i)

blockchain.stats()

