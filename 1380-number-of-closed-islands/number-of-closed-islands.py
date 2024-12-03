class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.visited = set()
        m, n = len(grid), len(grid[0])
        self.count = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def bfs(row, col):
            isClosed = True
            q = deque()
            q.append((row,col))
            self.visited.add((row,col))

            while q:
                r,c = q.popleft()

                if r in [0, m-1] or c in [0, n-1]:
                    isClosed = False
                for dr, dc in directions:
                    newr, newc = r+dr, c+dc
                    if 0<=newr<m and 0<=newc<n and grid[newr][newc] == 0 and (newr,newc) not in self.visited:
                        q.append((newr,newc))
                        self.visited.add((newr,newc))
            if isClosed:
                self.count+=1
            # self.count += isClosed == True



        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0 and (row,col) not in self.visited:
                    print(row, " ", col)
                    bfs(row, col)
        return self.count