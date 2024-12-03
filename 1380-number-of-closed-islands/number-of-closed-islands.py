class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.visited = set()
        m, n = len(grid), len(grid[0])
        self.count = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(row, col):

            self.visited.add((row,col))

            if row in [0,m-1] or col in [0, n-1]:
                self.isClosed = False

            for dr, dc in directions:
                newr, newc = row+dr, col+dc
                if 0<=newr<m and 0<=newc<n and grid[newr][newc] == 0 and (newr,newc) not in self.visited:
                    dfs(newr,newc)
            
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0 and (row,col) not in self.visited:
                    self.isClosed = True
                    dfs(row,col)
                    if self.isClosed:
                        self.count+=1
                    # self.count += self.isClosed == True
        return self.count