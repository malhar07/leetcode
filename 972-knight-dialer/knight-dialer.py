class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = {
            0:[6,4],
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[0,3,9],
            5:[],
            6:[0,1,7],
            7:[2,6],
            8:[1,3],
            9:[2,4]
        }
        dp = [[1]* 10 for _ in range(2)]
        for num in range(2, n+1):
            for i in range(10):
                curr = 0
                for nei in moves[i]:
                    curr+=dp[0][nei]
                dp[1][i] = curr
            dp[0] = dp[1][:]
        return sum(dp[0]) % MOD





#     1 2 3 4 5 6 7 8 9 0
# 1   1 1 1 1 1 1 1 1 1 1
# 2   2 2 2 3 0 3 2 2 2 2
# 3
# 4
# 5
# 6