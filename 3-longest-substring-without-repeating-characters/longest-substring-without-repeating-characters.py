class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict1 = {}
        res = 0
        left = 0
        for ind in range(len(s)):
            if s[ind] in dict1:
                res = max(res, ind-left)
                while s[ind] in dict1:
                    del dict1[s[left]]
                    left+=1
            # else:
            dict1[s[ind]] = ind
        # print(ind)
        return max(res, len(s) - left )
        return res
