class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        highest_price = prices[-1]

        for i in range(len(prices)-2,-1,-1):
            print(highest_price, " ", prices[i])
            profit = max(profit, highest_price-prices[i])
            highest_price = max(highest_price, prices[i])
        return profit