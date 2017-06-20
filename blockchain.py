import logging

import json
import datetime

from block import Block
from mining import generate_block

class Blockchain(object):

    def __init__(self):
        logging.debug("Initializing the blockchain")
        self.blockchain = [Block.get_genesis_block()]

    def generate_next_block(self, block_data=None):
        self.blockchain.append(generate_block(self.last_block(), block_data))

    def last_block(self):
        return self.blockchain[-1]

    def is_valid_chain(self, new_blocks):
        for i, block in enumerate(new_blocks):
            if i == 0:
                if (json.dumps(block) != json.dumps(self.blockchain[i])):
                    logging.error("Genesis blocks are not the same")
                    return False
            elif not block.is_valid_block(new_blocks[i-1]):
                logging.error("Invalid block")
                return False

        return True

    def replace_chain(self, new_blocks):
        if self.is_valid_chain(new_blocks) and len(new_blocks) > len(self.blockchain):
            logging.info("Received new valid blockchain, replacing...");
            self.blockchain = new_blocks
            self.broadcast()
        else:
            logging.error("Received invalid blockchain");

    def broadcast(self):
        logging.info("TODO: Notifying peers");

