class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1]*len(nums)
        def helper(ind):
            if ind>=len(nums):
                return 0
            if memo[ind]==-1:
                memo[ind] = max(helper(ind+1), nums[ind]+helper(ind+2))
            return memo[ind]
        return helper(0)
            