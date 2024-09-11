class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dict1 = {}
        res = -1

        for ind, i in enumerate(s):
            if i in dict1:
                res = max(res, ind-dict1[i]-1)
            else:
                dict1[i] = ind
        return res