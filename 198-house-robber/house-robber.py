class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * len(nums)

        def dfs(ind):
            if ind>=n:
                return 0
            if memo[ind] != -1:
                return memo[ind]
            rob_curr = nums[ind] + dfs(ind+2)
            skip = dfs(ind+1)
            if memo[ind] == -1:
                memo[ind] = max(skip, rob_curr)
            return memo[ind]
        return dfs(0)
            