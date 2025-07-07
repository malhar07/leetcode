class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols, res = m, n, 0
        memo = [[0]*(cols+1) for _ in range(rows+1)]
        # memo[rows-1][cols] = 0
        memo[rows][cols-1] = 1
        print(memo)
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                memo[r][c] = memo[r+1][c] + memo[r][c+1]
        return memo[0][0]

# [0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 1], 
# [0, 0, 0, 0, 0, 0, 1, 0]]