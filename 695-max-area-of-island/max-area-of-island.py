class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        length = len(grid)
        width = len(grid[0])
        res = 0
        visited = set()

        def bfs(x,y):
            q = deque([(x,y)])
            visited.add((x,y))

            directions = [[0,1], [1,0], [0,-1], [-1,0]]
            size = 1

            while q:
                x,y = q.popleft()
                for dr, dc in directions:
                    newr, newc = x+dr, y+dc

                    if 0<=newr<length and 0<=newc<width and (newr,newc) not in visited and grid[newr][newc]==1:
                        q.append((newr, newc))
                        visited.add((newr, newc))
                        size+=1
            return size


        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1 and (i,j) not in visited:
                    res = max(res, bfs(i,j))
        return res
