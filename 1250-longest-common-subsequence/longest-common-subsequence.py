class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {} #(ind1,ind2) -> LCS
        
        def dfs(text1, text2, ind1, ind2):
            if ind1 == len(text1) or ind2 == len(text2):
                return 0
            if (ind1,ind2) not in memo:
                lcs = 0
                if text1[ind1] == text2[ind2]:
                    lcs =  1 + dfs(text1, text2, ind1+1, ind2+1)
                else:
                    lcs =  max(dfs(text1,text2,ind1+1,ind2), dfs(text1,text2, ind1, ind2+1))
                memo[(ind1,ind2)] = lcs
            return memo[(ind1,ind2)]
        return dfs(text1, text2, 0, 0)
