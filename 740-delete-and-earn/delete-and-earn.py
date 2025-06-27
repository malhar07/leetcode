class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        # nums.sort()
        dp = [0]*(max(nums)+2)
        dp[max(nums)] = count[max(nums)]*max(nums)
        [1,3,6]

        # dp = [0]*(max(nums)+1)
        for i in range(max(nums)-1, 0, -1):
            if i not in count:
                curr_points = 0
            else:
                curr_points = count[i]*i
            dp[i] = max(dp[i+1], curr_points+dp[i+2])
        return dp[1]
