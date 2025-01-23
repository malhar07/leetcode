class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = [0]*26
        res = 0
        for i in range(len(s)):
            count[ord(s[i]) - ord('A')] += 1
            # print(count, " ", left)

            if ((i+1) - left) - max(count) <= k:
                res = i+1 - left
            else:
                
                count[ord(s[left]) - ord('A')] -= 1
                left+=1
        return res