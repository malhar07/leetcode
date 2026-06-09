class MyHashMap:

    def __init__(self):
        self.map = [-1]*1000

    def put(self, key: int, value: int) -> None:
        hash_val = key%1000
        
        if self.map[hash_val] == -1:
            self.map[hash_val] = []

        arr = self.map[hash_val]

        for i in range(len(arr)):
            k,v = arr[i]
            if k == key:
                arr[i] = (key,value)
                return
        self.map[hash_val].append((key,value))

            

    def get(self, key: int) -> int:
        hash_val = key%1000
        if self.map[hash_val] == -1:
            return -1
        else:
            for hash_key,val in self.map[hash_val]:
                if hash_key == key:
                    return val
        return -1

    def remove(self, key: int) -> None:
        hash_val = key%1000
        if self.map[hash_val] != -1:
            for index, tup in enumerate(self.map[hash_val]):
                hash_key, val = tup
                if hash_key == key:
                    self.map[hash_val].pop(index)
                    return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)