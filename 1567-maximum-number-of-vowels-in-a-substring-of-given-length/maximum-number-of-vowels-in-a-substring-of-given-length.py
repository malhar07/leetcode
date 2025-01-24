class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        res = 0
        left = 0
        curr = 0
        for i in range(k-1):
            if s[i] in vowels:
                curr+=1

        for i in range(k-1, len(s)):
            if s[i] in vowels:
                # print(curr)
                curr+=1

            res = max(res, curr)

            if s[left] in vowels:
                print(left)
                curr-=1
            left+=1
        return res
            