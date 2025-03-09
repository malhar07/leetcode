class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(arr, ind):
            
            if len(arr) == len(nums):
                res.append(arr[:])
                return 
            if ind >= len(nums):
                return 
            
            for i in range(len(arr)+1):
                helper(arr[:i] + [nums[ind]] + arr[i:], ind+1)
        helper([],0)
        return res