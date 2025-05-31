class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = 0
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        visited = set()

        def bfs(r,c):
            nei = [[r,c]]
            size = 1

            while nei:
                r,c = nei.pop()

                for dr, dc in dirs:
                    newr, newc = r+dr, c+dc

                    if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and grid[newr][newc]==1 and (newr,newc) not in visited:
                        nei.append((newr,newc))
                        visited.add((newr,newc))
                        size+=1
            return size
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited.add((i,j))
                    max_size = max(max_size, bfs(i,j))
        return max_size



