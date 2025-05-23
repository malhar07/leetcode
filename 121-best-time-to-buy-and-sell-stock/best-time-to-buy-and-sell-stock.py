class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_right = [0]*len(prices)
        # max_right[-1] = prices[-1]
        # for i in range(len(prices)-2, -1, -1):
        #     max_right[i] = max(max_right[i+1], prices[i])
        # res = 0
        # for i in range(len(prices)):
        #     res = max(res, max_right[i]- prices[i])
        # return res
        left = 0
        res = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[left]:
                left = i
            else:
                res = max(res, prices[i]- prices[left])
        return res
