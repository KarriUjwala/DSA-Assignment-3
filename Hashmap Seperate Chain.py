class SeparateChainingHashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(capacity)]

    def hash(self, key):
        return key % self.capacity

    def insert(self, key, value):
        idx = self.hash(key)
        for kv in self.table[idx]:
            if kv[0] == key:
                kv[1] = value
                return
        self.table[idx].append([key, value])
        self.size += 1

    def find(self, key):
        idx = self.hash(key)
        for kv in self.table[idx]:
            if kv[0] == key:
                return True
        return False

    def remove(self, key):
        idx = self.hash(key)
        self.table[idx] = [kv for kv in self.table[idx] if kv[0] != key]
        self.size -= 1
