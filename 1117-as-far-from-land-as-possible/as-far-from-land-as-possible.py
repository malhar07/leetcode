class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        visited = set()
        n = len(grid)
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    visited.add((row,col))
        def bfs():
            q = deque(visited)
            dist = -1
            while q:
                dist+=1
                for i in range(len(q)):
                    row, col  = q.popleft()
                    for dr, dc in directions:
                        newr, newc = row+dr, col+dc
                        if 0<=newr<n and 0<=newc<n and (newr, newc) not in visited:
                            q.append((newr, newc))
                            visited.add((newr, newc))
            return dist


        dist = bfs()
        return -1 if dist == 0 else dist