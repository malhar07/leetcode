class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = [[-1]*n for _ in range(m)]
        
        def dfs(text1, text2, ind1, ind2):
            if ind1 == len(text1) or ind2 == len(text2):
                return 0
            if memo[ind1][ind2]!=-1:
                return memo[ind1][ind2]
            if text1[ind1] == text2[ind2]:
                memo[ind1][ind2] =  1 + dfs(text1, text2, ind1+1, ind2+1)
            else:
                memo[ind1][ind2] =  max(dfs(text1,text2,ind1+1,ind2), dfs(text1,text2, ind1, ind2+1))
            return memo[ind1][ind2]
        return dfs(text1, text2, 0, 0)
