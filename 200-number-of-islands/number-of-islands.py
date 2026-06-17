class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        def dfs(r,c):
            if not 0<=r<len(grid) or not 0<= c < len(grid[0]):
                return
            grid[r][c] = "0"

            for dr, dc in directions:
                if 0<=r+dr<len(grid) and 0<=c+dc<len(grid[0]) and grid[r+dr][c+dc]=="1":
                    dfs(r+dr, c+dc)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands+=1
        
        return islands