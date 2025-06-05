class Solution:
    def rob(self, nums: List[int]) -> int:
        left, right = 0, 0
        # temp
        for i in range(len(nums)):
            curr = max(nums[i]+left, right)

            left = right
            right = curr
        return right