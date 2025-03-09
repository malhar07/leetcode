class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        def dfs(x,y):
            # q = deque([(x,y)])
            visited.add((x,y))

            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            for dr, dc in directions:
                newx,newy = x+ dr, y+dc
                if 0<=newx<len(grid) and 0<=newy<len(grid[0]) and (newx,newy) not in visited and grid[newx][newy] == "1":       
                    visited.add((newx, newy))
                    dfs(newx, newy)
                

        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    islands += 1
                    dfs(i,j)
        return islands
