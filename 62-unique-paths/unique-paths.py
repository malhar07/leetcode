class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols, res = m, n, 0
        memo = [[-1]*cols for _ in range(rows)]
        memo[rows-1][cols-1] = 1
        def dfs(r,c):
            if r>=rows or c>=cols:
                return 0
            
            if memo[r][c] == -1:
                memo[r][c] = dfs(r+1,c) + dfs(r,c+1)
                            
            return memo[r][c]
        return dfs(0,0)
            