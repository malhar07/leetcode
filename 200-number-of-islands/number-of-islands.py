class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = set()
        
        def bfs(r,c):
            q = deque([(r,c)])

            while q:
                r,c = q.popleft()

                for dr,dc in dirs:
                    newr, newc = r+dr, c+dc
                    if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and (newr,newc) not in visited and grid[newr][newc] == "1":
                        q.append((newr,newc))
                        visited.add((newr,newc))
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    visited.add((i,j))
                    bfs(i,j)
                    count+=1
        return count