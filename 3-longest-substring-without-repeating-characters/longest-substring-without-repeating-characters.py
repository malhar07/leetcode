class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        curr_longest = 0
        longest_sub = 0
        chars = set()
        while right<len(s):
            if s[right] in chars:
                longest_sub = max(longest_sub, curr_longest)
                while s[left] != s[right]:
                    chars.remove(s[left])
                    left+=1
                    curr_longest-=1
                chars.remove(s[left])
                left+=1
                curr_longest-=1

            curr_longest +=1
            chars.add(s[right])
            right+=1
        return max(longest_sub, curr_longest)