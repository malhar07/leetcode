class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        chars = set()

        for i in range(len(s)):
            chars = set()
            for j in range(i, len(s)):
                # print(chars)
                if s[j] in chars:
                    
                    break
                else:
                    chars.add(s[j])
            res = max(res, len(chars))
        return res
