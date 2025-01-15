class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0],0)]
        res = [0]*len(temperatures)

        for i in range(1,len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                ele = stack.pop()
                res[ele[1]] = i-ele[1]
            stack.append((temperatures[i],i))
        return res
        