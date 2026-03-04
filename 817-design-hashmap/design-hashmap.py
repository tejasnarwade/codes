class MyHashMap:

    def __init__(self):
        self.hm =[]

        

    def put(self, key: int, value: int) -> None:
        for pair in self.hm:
            if pair[0]==key:
                pair[1]=value
                return
        self.hm.append([key,value])


    def get(self, key: int) -> int:
        for r in range(len(self.hm)):
            if self.hm[r][0]==key:
                return int(self.hm[r][1])
        return -1
        

    def remove(self, key: int) -> None:
        self.hm = [pair for pair in self.hm if pair[0]!=key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)