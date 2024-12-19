class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []

        for ind, i in enumerate(position):
            arr.append((i, (target-i)/speed[ind]))

        arr = sorted(arr,key = lambda x:x[0])
        fleets = 1
        curr = arr[-1][1]
        for i in range(len(arr)-1, -1, -1):
            if arr[i][1] > curr:
                curr = arr[i][1]
                fleets+=1
        return fleets

