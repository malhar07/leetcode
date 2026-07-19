class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        memo = {}

        def backtrack(ind):
            if ind >= len(s):
                return True
            if ind in memo:
                return memo[ind]

            for i in range(ind, len(s)):
                curr = s[ind:i+1]
                if curr in wordset:
                    print(curr)
                    if backtrack(i+1):
                        return True
                    else:
                        memo[i+1] = False
            memo[ind] = False
            return False

        return backtrack(0)          