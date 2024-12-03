class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        arr = [0] * n
        for edge in edges:
            arr[edge[1]] = 1
        res = []
        for i in range(len(arr)):
            if arr[i] == 0:
                res.append(i)
        return res