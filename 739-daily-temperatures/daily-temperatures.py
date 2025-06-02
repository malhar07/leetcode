class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)

        stack = [(temperatures[0], 0)]

        for i in range(1,len(temperatures)):
            # if temperatures[i] <= stack[i][0]:
                
            # else:
                while stack and temperatures[i] > stack[-1][0]:
                    curr = stack.pop()
                    res[curr[1]] = i - curr[1]
                stack.append((temperatures[i],i))
        return res