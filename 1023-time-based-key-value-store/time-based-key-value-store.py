class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map[key]
        # if not arr or (arr and arr[0][1] > timestamp):
        #     return ""
        left = 0
        right = len(arr)-1
        res = ""

        while left<=right:
            mid = left + (right-left)//2

            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                left = mid+1
            else:
                right = mid-1
        return res


        # for i in range(len(arr)-1,-1,-1):
        #     if arr[i][1] <= timestamp:
        #         return arr[i][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)