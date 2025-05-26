class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ind1, ind2 = 0, 0
        res = []

        while ind1 < len(word1) and ind2 < len(word2):
            res.append(word1[ind1])
            res.append(word2[ind2])
            ind1+=1
            ind2+=1
        if ind1 < len(word1):
            res.append(word1[ind1:])
        else:
            res.append(word2[ind2:])
        return "".join(res)