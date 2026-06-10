class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        arr = [0]*len(prices)
        curr_max = prices[-1]
        for i in range(len(prices)-1,-1,-1):
            curr_max = max(curr_max, prices[i])
            arr[i] = curr_max
        for i in range(len(prices)):
            profit = max(profit, arr[i] - prices[i])
        return profit