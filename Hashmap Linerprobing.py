class LinearProbingHashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [(-1, -1)] * capacity
        self.isOccupied = [False] * capacity

    def hash(self, key):
        return key % self.capacity

    def probe(self, key, i):
        return (self.hash(key) + i) % self.capacity

    def insert(self, key, value):
        if self.size >= self.capacity:
            print("HashMap is full")
            return
        i = 0
        while True:
            idx = self.probe(key, i)
            if not self.isOccupied[idx] or self.table[idx][0] == key:
                break
            i += 1
        if not self.isOccupied[idx]:
            self.size += 1
        self.table[idx] = (key, value)
        self.isOccupied[idx] = True

    def find(self, key):
        i = 0
        while True:
            idx = self.probe(key, i)
            if not self.isOccupied[idx]:
                return False
            if self.table[idx][0] == key:
                return True
            i += 1

    def remove(self, key):
        i = 0
        while True:
            idx = self.probe(key, i)
            if not self.isOccupied[idx]:
                return
            if self.table[idx][0] == key:
                self.isOccupied[idx] = False
                self.size -= 1
                return
            i += 1
