class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind = 0
        for i in range(len(t)):
            if ind>len(s)-1:
                return True
            if s[ind] == t[i]:
                ind+=1
        if ind>len(s)-1:
                return True
        return False
            