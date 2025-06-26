class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo = [-1]*len(nums)

        # def helper(ind):
        #     if ind>=len(nums):
        #         return 0
        #     if memo[ind]==-1:
        #         memo[ind] = max(helper(ind+1), nums[ind]+helper(ind+2))
        #     return memo[ind]
        # return helper(0)
        if len(nums) == 1:
            return nums[0]
        dp = [nums[-2], nums[-1]]
        for i in range(len(nums)-3, -1, -1):
            curr = max(nums[i] + dp[1], dp[0])
            dp[1], dp[0] = max(dp[0],dp[1]), curr
        return max(dp)
            