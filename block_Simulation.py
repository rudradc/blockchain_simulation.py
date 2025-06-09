import hashlib
import time

# Define the Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index                          # Block position in the chain
        self.timestamp = timestamp                  # Timestamp of creation
        self.data = data                            # Block's transaction or message
        self.previous_hash = previous_hash          # Hash of the previous block
        self.nonce = 0                              # A number used to vary the hash (for PoW)
        self.hash = self.calculate_hash()           # Current block's hash

    # Method to calculate hash using SHA-256
    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

# Create the blockchain as a list
blockchain = []

# Create the genesis block (first block)
genesis_block = Block(0, time.ctime(), "Genesis Block", "0")
blockchain.append(genesis_block)

# Create two more linked blocks
block1 = Block(1, time.ctime(), {"amount": 100}, genesis_block.hash)
blockchain.append(block1)

block2 = Block(2, time.ctime(), {"amount": 50}, block1.hash)
blockchain.append(block2)

# Display the blockchain before tampering
print("Blockchain Before Tampering:\n")
for block in blockchain:
    print(f"Block {block.index}:\nHash: {block.hash}\nData: {block.data}\nPrevious Hash: {block.previous_hash}\n")

# ------------ CHALLENGE: Tampering Block 1 ------------ #
print("\nTampering Block 1...\n")

# Change the data in block1
blockchain[1].data = {"amount": 999}
blockchain[1].hash = blockchain[1].calculate_hash()

# Update block2's previous hash and recalculate its hash
blockchain[2].previous_hash = blockchain[1].hash
blockchain[2].hash = blockchain[2].calculate_hash()

# Display the blockchain after tampering
print("Blockchain After Tampering:\n")
for block in blockchain:
    print(f"Block {block.index}:\nHash: {block.hash}\nData: {block.data}\nPrevious Hash: {block.previous_hash}\n")

# ------------ Function to Validate Blockchain ------------ #
def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current = chain[i]
        previous = chain[i - 1]

        # Check if current hash is correct
        if current.hash != current.calculate_hash():
            return False

        # Check if previous hash matches
        if current.previous_hash != previous.hash:
            return False

    return True

# Check chain validity
print("Is Blockchain Valid?", is_chain_valid(blockchain))
