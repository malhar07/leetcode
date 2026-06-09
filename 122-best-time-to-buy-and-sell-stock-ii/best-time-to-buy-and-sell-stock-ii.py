class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = [0]*len(prices)
        arr[-1] = prices[-1]
        res = 0
        for i in range(len(prices)-2,-1,-1):
            arr[i] = max(prices[i], arr[i+1])
        
        curr_max = arr[-1]
        for i in range(len(prices)-2,-1,-1):
            if prices[i] < curr_max:
                res += curr_max - prices[i]
            # else:
            curr_max = prices[i]
        return res
