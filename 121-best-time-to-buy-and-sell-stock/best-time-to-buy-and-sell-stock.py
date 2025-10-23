class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = 10001
        for p in prices:
            if p <= lowest:
                lowest = p
            else:
                res = max(res, p-lowest)
        return res
