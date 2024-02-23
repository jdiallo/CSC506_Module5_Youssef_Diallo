# #CSC 506 module 5
# Second example

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        if self.hash_table[index] is None:
            self.hash_table[index] = key
        else:
            while self.hash_table[index] is not None:
                index = (index + 1) % self.size
            self.hash_table[index] = key

    def display(self):
        print("Hash Table:")
        for i in range(self.size):
            print(f"Index {i}: {self.hash_table[i]}")

# Example usage
hash_table = HashTable(10)
keys = [12, 22, 32, 42, 52, 62, 72]

for key in keys:
    hash_table.insert(key)

hash_table.display()

