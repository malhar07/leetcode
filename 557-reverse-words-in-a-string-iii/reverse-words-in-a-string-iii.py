class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()

        res = ""

        for i in arr:
            res += i[::-1] + " "
        return res[:-1]