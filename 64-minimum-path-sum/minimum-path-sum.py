class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = {(rows-1,cols-1):grid[rows-1][cols-1]}
        def dfs(r,c):
            if r == rows or c == cols:
                return math.inf
            if (r,c) not in memo:
                memo[(r,c)] = grid[r][c] + min(dfs(r+1,c), dfs(r,c+1))
            
            return  memo[(r,c)]
        return dfs(0,0)