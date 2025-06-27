class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        nums = list(set(nums))
        nums.sort()

        dp = [0]*len(nums)
        dp[0] = nums[0]*count[nums[0]]

        # [2,3,4]

        for i in range(1,len(nums)):
            prev = dp[i-1]
            if nums[i] == nums[i-1]+1:
                if i-2>=0:
                    prev = dp[i-2]
                else:
                    prev = 0
            dp[i] = max((nums[i]*count[nums[i]] + prev), dp[i-1])
        
        return dp[-1]
