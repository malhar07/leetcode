# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         dict1 = {}
#         res = 0
#         left = 0
#         for i in range(len(s)):
#             if s
#             if s[i] in dict1:
#                 res = max(res, i - dict1[s[i]])
#                 left = i
#                 while s[i] in dict1:
#                     del dict1[s[left]]
#                     left+=1
#             # else:
#             dict1[s[i]] = i
#         return max(res,len(s)-left+1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            char_index[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length

