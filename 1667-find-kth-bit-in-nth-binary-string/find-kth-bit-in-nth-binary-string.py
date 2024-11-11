class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            t = ""
            for i in s:
                if i == "1":
                    t+="0"
                else:
                    t+="1"
            return t
        def helper(n):
            if n == 1:
                return "0"
            s = helper(n-1)
            return s + "1" + invert(s)[::-1]
        return helper(n)[k-1]