class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        path = set()

        def dfs(row, col, gold):
            gold += grid[row][col]
            path.add((row,col))
            max_gold = gold

            for r, c in directions:
                newr, newc = row+r, col+c
                if 0<=newr<m and 0<=newc<n and grid[newr][newc] != 0 and (newr, newc) not in path:
                    max_gold = max(max_gold, dfs(newr, newc, gold))
            path.remove((row, col))

            return max_gold




        res = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] != 0:
                    res = max(res, dfs(row, col, 0))
        return res
