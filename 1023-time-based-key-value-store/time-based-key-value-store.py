class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        arr = self.time_map[key]
        right = len(arr) -1 
        res = ""
        # curr = -1
        # print(arr)

        while left<=right:
            
            mid = (left+right)//2
            # print(mid)


            if arr[mid][1] > timestamp:
                right = mid-1
            elif arr[mid][1] < timestamp:
                res = arr[mid][0]
                # curr = mid
                left = mid+1
            else:
                return arr[mid][0]
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)