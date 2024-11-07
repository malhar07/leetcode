class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ind = 0
        curr = ""
        res = ""
        while True:
            if ind>= len(strs[0]):
                return res
            curr = strs[0][ind]
            for word in strs:
                if ind >= len(word) or word[ind] != curr:
                    return res
            ind+=1
            res += curr