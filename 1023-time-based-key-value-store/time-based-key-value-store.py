class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp)) # [key, timestamp]
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map[key]
        if not arr or timestamp < arr[0][1]:
            return ""
        
        left = 0
        right = len(arr)-1

        while left <= right:
            mid = left + (right-left)//2

            if arr[mid][1] > timestamp:
                right = mid-1
            elif arr[mid][1] < timestamp:
                res = arr[mid][0]
                left = mid+1
            else:
                return arr[mid][0]
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)