class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for ind, i in enumerate(temperatures):
            if stack:
                while stack and  i > stack[-1][0]:
                    temp, index = stack.pop()
                    res[index] = ind -  index
                    # stack.pop()
            stack.append((i, ind))
        return res
        