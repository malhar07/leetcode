class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        res = len(nums)+1
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            while left <= right and curr_sum >= target:
                res = min(res, right-left+1)
                curr_sum -= nums[left]
                left += 1
        if res > len(nums):
            return 0
        return res