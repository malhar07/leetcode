class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        path = set()

        def dfs(row, col):
            self.gold += grid[row][col]
            
            if self.max_gold == 0:
                self.max_gold = self.gold
            else:
                self.max_gold = max(self.max_gold, self.gold)
            

            path.add((row,col))
            for r, c in directions:
                newr, newc = row+r, col+c
                if 0<=newr<m and 0<=newc<n and grid[newr][newc] != 0 and (newr, newc) not in path:
                    path.add((newr, newc))
                    dfs(newr, newc)
            self.gold -= grid[row][col]
            path.remove((row, col))

            return self.max_gold




        res = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] != 0:
                    self.gold = 0
                    self.max_gold = 0
                    res = max(res, dfs(row, col))
        return res
