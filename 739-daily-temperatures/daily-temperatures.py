class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                res[stack[-1][0]] = ind-stack[-1][0]
                stack.pop()
            stack.append((ind, temp))
        return res
