class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def house(nums):
            memo = [0,0]
            for i in range(len(nums)-1,-1,-1):
                curr = max((nums[i] + memo[1]), memo[0])
                memo[1] = memo[0]
                memo[0] = curr
            return memo[0]
        return max(house(nums[:-1]), house(nums[1:]))
