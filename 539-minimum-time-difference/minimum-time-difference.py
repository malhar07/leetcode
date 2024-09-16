class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        res = 1441
        arr = []
        for i in timePoints:
            time = i.split(":")
            # if time[0] == "00":
            #     arr.append(1440 + int(time[1]))
            x = int(time[0])*60 + int(time[1])
            arr.append(x)
            arr.append(1440 + x)
        # arr.append(60)
        # print(arr)
        arr.sort()
        for i in range(1, len(arr)):
            res = min(res, arr[i] - arr[i-1])
        return res