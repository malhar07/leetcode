class TimeMap:

    def __init__(self):
        self.dict1 = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict1:
            self.dict1[key] = []
        self.dict1[key].append((value, timestamp))
    def get(self, key: str, timestamp: int) -> str:

        if key not in self.dict1:
            return ""
        else:
            arr = self.dict1[key]
            for i in range(len(arr)-1,-1,-1):
                if timestamp>=arr[i][1]:
                    return arr[i][0]
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)