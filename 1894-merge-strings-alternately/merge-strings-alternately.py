class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ind1 = 0
        ind2 = 0
        res = ""

        while ind1 < len(word1) and ind2 < len(word2):
            res += word1[ind1] + word2[ind2]
            ind1 +=1
            ind2+=1
        if ind1< len(word1):
            res += word1[ind1:]
        if ind2 < len(word2):
            res += word2[ind2:]
        return res