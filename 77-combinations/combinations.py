class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(arr, ind):
            if len(arr) == k:
                res.append(arr[:])
                return
            if ind > n:
                return
            
            arr.append(ind)
            helper(arr,ind+1)
            arr.pop()
            helper(arr, ind+1)
        helper([],1)
        return res