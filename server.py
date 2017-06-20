import blockchain

bc = blockchain.Blockchain()

for i in range(1000):
    bc.generate_next_block("block data = %d" % i)

bc.stats()

