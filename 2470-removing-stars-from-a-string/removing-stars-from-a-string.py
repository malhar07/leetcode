class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            stack.append(i)
        res = ""
        count = 0
        while stack:
            ele = stack.pop()
            if ele == "*":
                count+=1
            else:
                if count == 0:
                    res += ele
                else:
                    count-=1
        return res[::-1]