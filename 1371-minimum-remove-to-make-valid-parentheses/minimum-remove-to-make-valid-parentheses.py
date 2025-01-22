class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_count = 0
        res = ""
        for i in s:
            if i not in ['(', ')']:
                res+=i
            else:
                if i == ')':
                    if open_count <= 0:
                        continue
                    else:
                        open_count-=1
                        res+=i
                else:
                    open_count += 1
                    res += i
        print(res, " ",open_count)
        s= res
        res = ""
        ind = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != "(" or open_count == 0:
                res+=s[i]
            else:
                open_count -=1
            
        return res[::-1]


