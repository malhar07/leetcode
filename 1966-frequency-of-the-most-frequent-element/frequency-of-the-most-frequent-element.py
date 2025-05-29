class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        diff = 0
        res = 1
        left = 0
        nums.sort()

        for right in range(1,len(nums)):
            diff += (nums[right] - nums[right-1]) * (right-left)
            if diff<=k:
                res = max(res, right-left+1)
            else:
                while left<= right and diff>k:
                    
                    diff-=nums[right]-nums[left]
                    left+=1
        return res

