class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = [prices[-1]]*len(prices)
        curr_max = prices[-1]
        for i in range(len(prices)-1,-1,-1):
            if prices[i]>curr_max:
                curr_max = prices[i]
            prices[i] = curr_max-prices[i]
        return max(prices)