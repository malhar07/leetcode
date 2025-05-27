class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26
        max_frequency = 0
        left = 0
        res = 0
        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            max_frequency = max(max_frequency, count[ord(s[right]) - ord('A')])
            if (right-left+1) - max_frequency <= k:
                print(s[right])
                
                res = (right-left+1)
                print(res)
            else:
                count[ord(s[left]) - ord('A')]-=1
                left += 1

        return res

