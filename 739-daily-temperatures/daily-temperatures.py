class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[-1],len(temperatures)-1)]
        res = [0]*len(temperatures)

        for i in range(len(temperatures)-2, -1, -1):
            if temperatures[i] >= stack[-1][0]:
                while stack and stack[-1][0]<= temperatures[i]:
                    stack.pop()
                if not stack:
                    res[i] = 0
                else:
                    res[i] = stack[-1][1] - i
            else: 
                res[i] = 1
            stack.append((temperatures[i], i))
        return res
                