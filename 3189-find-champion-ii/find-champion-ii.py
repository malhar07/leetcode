class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        arr = [True]*n

        for strong, weak in edges:
            arr[weak] = False
        champion = -1
        for ind in range(len(arr)):
            if arr[ind] == True:
                if champion!=-1:
                    return -1
                champion = ind
        return champion