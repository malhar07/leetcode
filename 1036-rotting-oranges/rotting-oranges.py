class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fresh = 0
        visited = set()
        minutes = 0
        q = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1
            

        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                directions = [[-1,0], [1,0], [0,-1], [0,1]]
                for dr, dc in directions:
                    if r+dr < 0 or r+dr >=len(grid) or c+dc < 0 or c+dc >= len(grid[0]) or (r+dr,c+dc) in visited or grid[r+dr][c+dc] != 1:
                        continue
                    fresh-=1
                    grid[r+dr][c+dc] = 2
                    q.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))
            if q:
                minutes+=1
   
        
        # for r in range(row):
        #     for c in range(col):
        #         if grid[r][c] == 1:
        #             return -1
        if fresh > 0:
            return -1
        return minutes