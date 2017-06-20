import logging
logging.basicConfig(level=logging.DEBUG)

import blockchain

logging.debug("Starting blockchain server");

bc = blockchain.Blockchain()

for i in range(10):
    bc.generate_next_block("block data = %d" % i)

bc.stats()

