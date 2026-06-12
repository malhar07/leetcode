class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        res = 0
        for right in range(len(s)):
            if s[right] not in char_set:
                char_set.add(s[right])
            else:
                res = max(res, right-left)
                while s[left] != s[right]:
                    char_set.remove(s[left])
                    left += 1
                left += 1
        return max(res, len(s)-left)
