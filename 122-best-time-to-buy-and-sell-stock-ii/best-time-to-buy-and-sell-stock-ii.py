class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        res = 0
        for p in prices:
            if stack and stack[-1] < p:
                res += p-stack[-1]
                stack.pop()
            stack.append(p)
        return res
