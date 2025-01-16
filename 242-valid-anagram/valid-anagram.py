class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1 = [0]*26

        for i in range(len(s)):
            dict1[ord(s[i])-97]+=1# = dict1.get(ord(s[i]-97),0)+1
            dict1[ord(t[i])-97]-=1# = dict1.get(ord(t[i]-97),0)-1
        print(dict1)
        
        for i in dict1:
            if i != 0:
                return False
        return True