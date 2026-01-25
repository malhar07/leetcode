class TimeMap:

    def __init__(self):
        self.dict1 = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict1[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict1[key]
        res = ""

        left = 0
        right = len(arr)-1

        while left<= right:
            mid = left + (right-left)//2
            t,k = arr[mid]
            if t<timestamp:
                res = k
                left = mid+1
            elif t> timestamp:
                right = mid-1
            else:
                return k
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)