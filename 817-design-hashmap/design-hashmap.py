class MyHashMap:

    def __init__(self):
        self.map = [None]*(10**6)
    # def hash(key):

        

    def put(self, key: int, value: int) -> None:
        self.map[key-1] = value

    def get(self, key: int) -> int:
        if self.map[key-1] != None:
            return self.map[key-1]
        return -1
        

    def remove(self, key: int) -> None:
        self.map[key-1] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)