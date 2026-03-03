class MyHashSet:

    def __init__(self):
        self.ht = []
        

    def add(self, key: int) -> None:
        if key not in self.ht:
            self.ht.append(key)

    def remove(self, key: int) -> None:
        if key in self.ht:
            self.ht.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.ht


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)