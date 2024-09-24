class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res1 = ""
        res2 = ""
        ind = len(s)-1
        count = 0
        while ind >= 0:
            if s[ind] != "#":
                if count > 0:
                    count-=1
                else:
                    res1 += s[ind]
            else:
                count+=1
            ind-=1
        ind = len(t)-1
        count = 0
        while ind >= 0:
            if t[ind] != "#":
                if count > 0:
                    count-=1
                else:
                    res2 += t[ind]
            else:
                count+=1
            ind-=1
        print(res1, " ->", res2)
        return res1 == res2