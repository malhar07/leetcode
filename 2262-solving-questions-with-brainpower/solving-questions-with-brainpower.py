class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        #  [[3,2],[4,3],[4,4],[2,5]]
        #  max((0+ ind+1), (3 + ind+2+1))
        # brute force
        # checks all possible combinations
        # TC = 2^n 
        # SC = n for recursion stack

        # memo = {}
        # def helper(ind):
        #     if ind >= len(questions):
        #         return 0
        #     if ind not in memo:
        #         memo[ind] =  max(helper(ind+1), questions[ind][0] + helper(ind+1+questions[ind][1]))
        #     return memo[ind]
        # return helper(0)
        max_bp = max([questions[i][1] for i in range(len(questions))])
        print(max_bp)
        dp = [0]*(len(questions)+max_bp+1)
        print(dp)
        # dp[len()]

        for i in range(len(questions)-1, -1, -1):
            dp[i] = max(dp[i+1], questions[i][0] + dp[i+1+questions[i][1]])
        return dp[0]