import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

import blockchain

logging.debug("Starting the blockchain server");

bc = blockchain.Blockchain()

for i in range(10):
    bc.generate_next_block("block data = %d" % i)

logging.debug("There are %d blocks in the blockchain" % len(bc.blockchain))
for i, block in enumerate(bc.blockchain):

    # Genesis block doesn't have previous block to do normal validation
    if i == 0:
        assert block.is_valid_hash(), "Invalid hash, block hash %s should be %s" % (block.hash, block.calculate_hash())
    else:
        assert block.is_valid_block(bc.blockchain[i-1]), "Invalid hash, block hash %s should be %s" % (block.hash, block.calculate_hash())

    logging.debug("%d\t%s\t%s\t%s" % (block.index, block.readable_timestamp, block.hash, block.data))

