class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        visited = set()
        
        def dfs(r,c):
            visited.add((r,c))

            for dr, dc in dirs:
                newr, newc = r+dr, c+dc

                if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and grid[newr][newc] == "1" and (newr,newc) not in visited:
                    dfs(newr,newc)

            return 
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    res+=1
        return res