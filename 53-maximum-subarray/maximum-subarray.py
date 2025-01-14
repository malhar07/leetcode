class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None
        presum = [nums[0]]
        for i in range(1,len(nums)):
            presum.append(nums[i] + presum[i-1])
        
        max_sum = -10001
        low = 0
        
        for i in presum:
            max_sum = max(max_sum, i-low)
            if i < low:
                low = i
                
        return max_sum
