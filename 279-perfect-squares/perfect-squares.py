class Solution:
    def numSquares(self, n: int) -> int:
        # arr = [x**2 for x in range(1,101)]
        dp = [n+1]*(n+1)
        # dp[1] = 1
        dp[0]=0

        for i in range(1,n+1):
            for sq in range(1,101):
                if sq**2 > i:
                    break
                dp[i] = min(dp[i], 1+dp[i-sq**2])
        return dp[n]
