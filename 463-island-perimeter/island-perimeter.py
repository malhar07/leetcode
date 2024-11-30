class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        path = set()
        row, col = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        # def bfs(row, col):
        #     q = deque()
        #     q.append((row,col))
        #     perimeter = 0

        #     path.add((row,col))

        #     while q:
        #         for i in range(len(q)):
        #             r,c = q.popleft()
        #             perimeter += 4

        #             for dr, dc in directions:
        #                 newr, newc = r+dr, c+dc
        #                 if 0<= newr< len(grid) and 0<= newc<len(grid[0]) and grid[newr][newc] == 1 and(newr,newc) not in path:
        #                     q.append((newr, newc))
        #                     path.add((newr, newc))
        #     return perimeter+2

        
        perimeter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perimeter+=4
                    for dr, dc in directions:
                        newr, newc = i+dr, j+dc
                        if 0<= newr< len(grid) and 0<= newc<len(grid[0]) and grid[newr][newc] == 1:
                            perimeter -= 1


        return perimeter