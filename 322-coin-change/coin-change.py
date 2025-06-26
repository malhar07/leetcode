class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf]*(amount+1)
        dp[0] = 0
        # coins.sort()
        for amt in range(1,amount+1):
            for coin in coins:
                if coin>amt:
                    continue
                dp[amt] = min(dp[amt], 1+dp[amt-coin])
        return dp[amount] if dp[amount] != math.inf else -1
        # def helper(rem):
        #     if rem<0:
        #         return math.inf
        #     if rem == 0:
        #         return 0
            
        #     for i in range(1,amount+1):

