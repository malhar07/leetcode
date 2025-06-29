class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s):True}

        memo[-1] = True
        def helper(ind):
            if ind in memo:
                return memo[ind]
            found = False
            for i in range(ind, len(s)):
                if s[ind:i+1] in wordDict:
                    if helper(i+1):
                        found = True
            memo[ind] = found
            return memo[ind]
        return helper(0)