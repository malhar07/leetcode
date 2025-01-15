class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        res = len(nums)+1
        for i in range(len(nums)):
            curr_sum += nums[i]

            while curr_sum >= target:
                res = min(res, i-left+1)
                
                curr_sum-=nums[left]
                left+=1
        return res if res<=len(nums) else 0