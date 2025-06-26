class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = math.inf
        memo = {}
        def helper(rem,count):
            if rem<0:
                return math.inf
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]

            res = math.inf
            for coin in coins:
                count = 1 + helper(rem-coin, count)
                
                if count != math.inf:
                    res = min(res,count)
            memo[rem] = res
            return res

        res = helper(amount,0)
        return res if res != math.inf else -1
