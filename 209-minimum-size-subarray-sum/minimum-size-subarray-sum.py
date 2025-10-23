class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 100001
        curr_sum = 0
        left = 0
        for right, num in enumerate(nums):
            curr_sum += nums[right]

            # if curr_sum >= target:
            #     res = min(res,right-left+1)
            
            while curr_sum >= target:
                res = min(res,right-left+1)
                curr_sum-=nums[left]
                left+=1
        return res if res <= len(nums) else 0
