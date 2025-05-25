class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        highest_price_to_right = [prices[-1]]*len(prices)

        for i in range(len(prices)-2,-1,-1):
            highest_price_to_right[i] = max(highest_price_to_right[i+1], prices[i+1])

        for i in range(len(prices)):
            profit = max(profit, highest_price_to_right[i] - prices[i])
        return profit