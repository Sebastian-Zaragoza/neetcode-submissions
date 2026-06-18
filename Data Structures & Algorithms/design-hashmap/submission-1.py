class MyHashMap:

    def __init__(self):
        self.hashmap = {}
        
    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value
        return None

    def get(self, key: int) -> int:
        return self.hashmap[key] if key in self.hashmap else -1

    def remove(self, key: int) -> None:
        if key in self.hashmap:
            del self.hashmap[key]
        return None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)