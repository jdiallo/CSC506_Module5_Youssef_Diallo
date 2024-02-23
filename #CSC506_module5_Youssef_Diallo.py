#CSC 506 module 5

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        # Simple modulo hash function
        return key % self.size

    def insert(self, key, value):
        index = self.hash(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

# Example usage
ht = HashTable(10)
ht.insert(12, "Python")
ht.insert(25, "Java")
ht.insert(33, "C++")

print(ht.search(12))  # Output: Python
print(ht.search(25))  # Output: Java
print(ht.search(33))  # Output: C++
