class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(ind, arr):
            if ind == len(nums):
                res.append(arr[:])
                return
            
            dfs(ind+1, arr)
            arr.append(nums[ind])
            dfs(ind+1, arr)
            arr.pop()
            
        dfs(0,[])
        return res