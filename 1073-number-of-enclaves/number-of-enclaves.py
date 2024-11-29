class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        
        def bfs(row, col):
            q = deque()
            q.append((row,col))
            path = set()
            path.add((row,col))

            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    grid[row][col] = 0
                    for dr, dc in directions:
                        newr, newc = row+dr, col+dc

                        if 0<=newr<m and 0<= newc < n and grid[newr][newc] == 1 and (newr, newc) not in path:
                            path.add((newr, newc))
                            q.append((newr, newc))
        
        for row in range(m):
            for col in range(n):
                if row in [0, m-1] or col in [0, n-1]:
                    
                    if grid[row][col] == 1:
                        print(row, " ", col)
                        bfs(row, col)
        res = 0
        for i in grid:
            res+=sum(i)
        return res