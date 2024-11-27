class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        n = len(grid)

        visited = set()
        def dfs(row,col):
            visited.add((row,col))

            for dr, dc in directions:
                if 0<=row+dr<n and 0<=col+dc<n and grid[row+dr][col+dc] == 1 and (row+dr, col+dc) not in visited:
                    dfs(row+dr, col+dc)
        
        def bfs():
            q = deque(visited)
            count = 0

            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr, dc in directions:
                        if not (0 <= r+dr < n) or not (0<= c+dc<n) or (r+dr, c+dc) in visited:
                            continue
                        if grid[r+dr][c+dc] == 0:
                            q.append((r+dr,c+dc))
                            visited.add((r+dr,c+dc))
                        else:
                            return count
                count+=1




        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    dfs(row, col)
                    return bfs()
