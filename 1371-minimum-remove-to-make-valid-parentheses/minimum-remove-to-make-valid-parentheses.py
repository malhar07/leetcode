class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_count = 0
        res = ""
        for i in s:
            if i == ')':
                if open_count == 0:
                    continue
                else:
                    open_count-=1
            elif i == "(":
                open_count += 1
            res += i
        s = res
        res = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] != "(" or open_count == 0:
                res+=s[i]
            else:
                open_count -=1
            
        return res[::-1]


