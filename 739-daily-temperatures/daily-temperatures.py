class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [ind, val]

        res = [0]*len(temperatures)

        for ind,temp in enumerate(temperatures):
            if stack and stack[-1][1] < temp:
                while stack and stack[-1][1] < temp:
                    i, v = stack.pop()
                    res[i] = ind-i
                
            stack.append([ind, temp])
        return res
