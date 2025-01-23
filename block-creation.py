import hashlib
import time

class Block:
    def __init__(self, index, phash, timestamp, data):
        self.index = index
        self.phash = phash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        string = str(self.index) + str(self.phash) + str(self.timestamp) + str(self.data)
        return hashlib.sha256(string.encode("utf-8")).hexdigest()

    def display(self):
        print(f"Block: #{self.index}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Previous hash: {self.phash}")
        print(f"Data: {self.data}")
        print(f"Hash: {self.hash}")
        print()

# Create and display the Genesis block
n=int(input("Enter number of blocks: "))
obj = Block(0, "0", time.time(), "Genesis block")
obj.display()
prevhash=obj.hash

for i in range(n):
    object=Block(i,prevhash,time.time(),f"{i} Block")
    prevhash=object.hash
    object.display()

