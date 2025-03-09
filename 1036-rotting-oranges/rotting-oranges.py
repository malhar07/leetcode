class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = -1
        visited = set()
        q = deque([])

        def bfs(q):
            directions = [[0,1],[1,0], [0,-1],[-1,0]]
            time = 0

            while q:
                for i in range(len(q)):
                    r,c = q.popleft()

                    for dr, dc in directions:
                        newr, newc = r+dr, c+dc

                        if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and grid[newr][newc] == 1 and (newr,newc) not in visited:
                            grid[newr][newc] = 2
                            q.append((newr,newc))
                            visited.add((newr,newc))
                time+=1
            return time

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
        # if len(q) == 0:
        #     return 0

        res = bfs(q)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return max(0, res-1)

