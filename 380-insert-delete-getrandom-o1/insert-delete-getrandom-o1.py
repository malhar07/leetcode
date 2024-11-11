import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.dict1 = {}
        self.pointer = 0

    def insert(self, val: int) -> bool:
        if val not in self.dict1:
            self.arr.append(val)
            self.dict1[val] = len(self.arr)-1
            self.pointer+=1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.dict1:
            return False
        ind = self.dict1[val]
        self.arr[ind], self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1], self.arr[ind]
        self.dict1[self.arr[ind]] = ind
        self.arr.pop()
        del self.dict1[val]
        self.pointer-=1

        
        return True

    def getRandom(self) -> int:
        random_index = random.randint(0, self.pointer-1)

        return self.arr[random_index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()