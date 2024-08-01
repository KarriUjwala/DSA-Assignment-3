class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []
        self.map = {}

    def moveToFront(self, key: int, value: int):
        self.cache.remove((key, value))
        self.cache.insert(0, (key, value))
        self.map[key] = 0
        for i, (k, v) in enumerate(self.cache):
            self.map[k] = i

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        value = self.cache[self.map[key]][1]
        self.moveToFront(key, value)
        return value

    def put(self, key: int, value: int):
        if key in self.map:
            self.moveToFront(key, value)
        else:
            if len(self.cache) == self.capacity:
                lruKey, lruValue = self.cache.pop()
                del self.map[lruKey]
            self.cache.insert(0, (key, value))
            self.map[key] = 0
            for i, (k, v) in enumerate(self.cache):
                self.map[k] = i
