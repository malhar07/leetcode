class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = [0]*26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            ind = ord(s[i]) - ord('a')
            char_count[ind] += 1
            ind2 = ord(t[i]) - ord('a')
            char_count[ind2] -= 1
        for i in char_count:
            if i != 0:
                return False
        return True