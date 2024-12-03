class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        start = 0
        for end in spaces:
            res += s[start:end] + " "
            start = end
        return res + s[start:]