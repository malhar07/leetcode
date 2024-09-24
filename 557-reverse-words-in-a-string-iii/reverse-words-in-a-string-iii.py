class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        start = 0
        end = 0

        while end < len(s):
            while end< len(s) and s[end] != " ":
                end += 1
            temp = end-1
            while temp >= start:
                res += s[temp]
                temp -= 1
            res+=" "
            start = end+1
            end += 1
        return res[:len(res)-1]
