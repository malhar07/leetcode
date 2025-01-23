class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = nums[0]
        left = 0
        res = 1

        for i in range(1, len(nums)):
            total += nums[i]
            if (nums[i] * (i-left+1)) - total <= k:
                res = i-left+1
            else:
                total-=nums[left]
                left += 1
        return res
            

