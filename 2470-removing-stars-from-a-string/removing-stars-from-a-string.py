class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        ind = 0

        while ind<len(s):
            if s[ind] != "*":
                stack.append(s[ind])
            else:
                stack.pop()
            ind+=1
        res = ""
        for i in stack:
            res += i
        return res
