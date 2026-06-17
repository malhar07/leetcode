class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        fresh = False
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh = True
                if grid[r][c] == 2:
                    q.append((r,c))
        if len(q) == 0 and not fresh:
            return 0
        
        def bfs():
            time = -1
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr,dc in directions:
                        newr, newc = r+dr, c+dc
                        if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and grid[newr][newc] == 1 and (newr, newc) not in visited:
                            q.append((newr, newc))
                            grid[newr][newc] = 2
                            # visited.add((newr,newc))
                time+=1

            return time


        time = bfs()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return time
