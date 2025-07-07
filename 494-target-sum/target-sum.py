class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(ind, total):
            if ind == len(nums):
                if total == target:
                    return 1
                return 0
            if (ind,total) not in memo:
                memo[(ind,total)] = dfs(ind+1, total+nums[ind]) + dfs(ind+1, total-nums[ind])
            return memo[(ind,total)]
        return dfs(0,0)