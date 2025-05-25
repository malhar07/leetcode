class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_p = 10001
        for i in prices:
            if i <= min_p:
                min_p = i
            else:
                profit += i-min_p
                min_p = i
        return profit
