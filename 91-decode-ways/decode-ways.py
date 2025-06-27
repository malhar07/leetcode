class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {"0":0}
        def dfs(ind):
            if ind == len(s):
                return 1
            if s[ind] == "0":
                return 0
            if ind not in memo:
                res = 0
                for i in range(ind,len(s)):
                    if int(s[ind:i+1]) <= 26:
                        res += dfs(i+1)
                memo[ind] = res
            return memo[ind]
        return dfs(0)
                