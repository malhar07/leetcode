class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ind1 = 0
        len1, len2 = len(word1), len(word2)
        res = ""
        while ind1<len1 and ind1<len2:
            res += word1[ind1] + word2[ind1]
            ind1+=1
        if ind1<len1:
            res+=word1[ind1:]
        elif ind1<len2:
            res+=word2[ind1:]
        return res