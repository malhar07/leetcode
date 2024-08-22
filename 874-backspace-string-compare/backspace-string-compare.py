class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = ""
        s2 = ""

        count = 0
        ind = len(s)-1

        while ind >= 0:
            if s[ind] != "#":
                if count == 0:
                    s1+=s[ind]
                else:
                    count-=1
            else:
                count+=1

            ind-=1
        
        count = 0
        ind = len(t)-1

        while ind >= 0:
            if t[ind] != "#":
                if count == 0:
                    s2+=t[ind]
                else:
                    count-=1
            else:
                count+=1

            ind-=1
        print(s1, " ->", s2)
        return s1==s2