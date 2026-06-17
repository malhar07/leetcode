class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        res = 0

        def dfs(r,c) -> int:
            visited.add((r,c))
            area = 0
            for dr, dc in directions:
                newr, newc = r+dr, c+dc
                if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and (newr,newc) not in visited and grid[newr][newc] == 1:
                    # visited.add((newr,newc))
                    area += dfs(newr,newc)
            
            return 1+area



            
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:

                    res = max(res, dfs(r,c))
        return res