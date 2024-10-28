class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # res = 0
        # chars = set()

        # for i in range(len(s)):
        #     chars = set()
        #     for j in range(i, len(s)):
        #         # print(chars)
        #         if s[j] in chars:
        #             break
        #         else:
        #             chars.add(s[j])
        #     res = max(res, len(chars))
        # return res

        left = 0
        right = 0
        chars = set()
        res = 0

        while right<len(s):
            if s[right] in chars:
                res = max(res, right-left)

                while s[left] != s[right]:
                    chars.remove(s[left])
                    left+=1

                
                chars.remove(s[left])
                left+=1

            else:
                chars.add(s[right])
                right+=1
        return max(res, right-left)