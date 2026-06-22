class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charDict = {}
        used = set()
        if len(s)!=len(t):
            return False
        
        index = 0
        while index<len(s):
            if s[index] in charDict:
                if charDict[s[index]] != t[index]:
                    return False
            else:
                if t[index] in used:
                    return False
                charDict[s[index]] = t[index]
                used.add(t[index])
            index+=1
        return True