class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        self.minutes = 0

        def bfs():
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            

            while q:
                for i in range(len(q)):
                    r,c  = q.popleft()

                    grid[r][c] = 2

                    for dr, dc in directions:
                        if 0<= r+dr < len(grid) and 0<= c+dc < len(grid[0]) and grid[r+dr][c+dc] == 1 and (r+dr, c+dc) not in visited:
                            q.append((r+dr, c+dc))
                            visited.add((r+dr, c+dc))
                
                self.minutes+=1
            # return minutes




        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row, col))
                    visited.add((row,col))
        bfs()

        
        for row in grid:
            if 1 in row:
                return -1
        return max(0, self.minutes-1)