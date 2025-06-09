import hashlib
import time

# --------------------------
# Define the Block structure
# --------------------------
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index                    # Position in the chain
        self.timestamp = time.ctime()         # Human-readable time of creation
        self.data = data                      # Block transaction/data
        self.previous_hash = previous_hash    # Hash of the previous block
        self.nonce = 0                        # Will be updated during mining
        self.hash = self.calculate_hash()     # Initially calculate the hash

    def calculate_hash(self):
        # Generate SHA-256 hash using block data + nonce
        block_contents = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_contents.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Perform Proof-of-Work mining: adjust nonce until hash starts with required 'difficulty' prefix.
        """
        target = '0' * difficulty  # Example: if difficulty = 4, target = "0000"
        print(f"⛏️  Mining block with difficulty '{target}'...")

        start_time = time.time()  # Start timer
        attempts = 0

        # Keep trying until hash meets the difficulty condition
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1

        end_time = time.time()  # End timer

        # Print mining stats
        print(f" Block mined!")
        print(f" Nonce found: {self.nonce}")
        print(f" Hash: {self.hash}")
        print(f" Time taken: {end_time - start_time:.4f} seconds")
        print(f" Attempts: {attempts}\n")

# --------------------------
# Simulate mining a block
# --------------------------
# Set difficulty level (try increasing to 5 or 6 later)
difficulty = 4

# Create a new block and mine it
new_block = Block(index=1, data="Transaction: Alice -> Bob", previous_hash="0000abcdef")
new_block.mine_block(difficulty)
