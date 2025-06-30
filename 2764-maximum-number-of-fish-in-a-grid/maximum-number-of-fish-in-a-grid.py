class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        max_count = 0
        visited = set()
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]

        def is_valid_neighbor(newr, newc):
            if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and grid[newr][newc]>0 and (newr,newc) not in visited:
                return True
            return False


        def dfs(r,c):
            visited.add((r,c))
            total = grid[r][c]
            for dr, dc in dirs:
                newr, newc = r+dr, c+dc
                if is_valid_neighbor(newr, newc):
                
                    total+=dfs(newr, newc)
            return total 

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0 and (r,c) not in visited:
                    max_count = max(max_count, dfs(r,c))
        return max_count