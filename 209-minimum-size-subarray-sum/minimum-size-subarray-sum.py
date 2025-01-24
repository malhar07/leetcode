class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        res = len(nums)+1
        left = 0

        for i in range(len(nums)):
            total += nums[i]
            # if total >= target:
            #     res = min(res, i-left+1)
            while total>=target:
                res = min(res, i-left+1)
                total-=nums[left]
                left+=1
                
        return res if res<=len(nums) else 0