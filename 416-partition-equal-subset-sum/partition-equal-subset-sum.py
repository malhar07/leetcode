class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        target = sum(nums)//2
        memo = {}
        def helper(ind, total):
            if total == target:
                return True
            if ind == len(nums):
                return False
            
            if (ind,total) not in memo:
                memo[(ind,total)] =  helper(ind+1, total+nums[ind]) or helper(ind+1, total)
            return memo[(ind,total)]

        return helper(0,0)