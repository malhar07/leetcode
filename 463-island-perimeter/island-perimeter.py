class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        def addPerimeter(r,c):
            perimeter = 4
            if r>0 and grid[r-1][c] == 1:
                perimeter -= 1
            if r<len(grid)-1 and grid[r+1][c]==1:
                perimeter -= 1
            if c >0 and grid[r][c-1] == 1:
                perimeter -= 1
            if c<len(grid[0])-1 and grid[r][c+1] == 1:
                perimeter -= 1
            return perimeter

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == 1:
                    res += addPerimeter(r,c)
        return res