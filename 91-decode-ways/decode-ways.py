class Solution:
    def numDecodings(self, s: str) -> int:
        dp1 = 1
        dp0 = 0 if s[-1] == "0" else 1

        for i in range(len(s)-2,-1,-1):
            curr = dp0
            if s[i] == "0":
                curr = 0
            
            
            elif int(s[i:i+2]) <= 26:
                curr += dp1
            dp1 = dp0
            dp0 = curr
        return dp0
