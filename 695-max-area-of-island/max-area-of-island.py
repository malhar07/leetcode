class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        res = 0


        def bfs(r,c) -> int:
            q = deque()
            q.append([r,c])
            # visited.add((r,c))
            area = 0
            while q:
                r,c = q.popleft()

                for dr, dc in directions:
                    newr, newc = r+dr, c+dc
                    if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and (newr,newc) not in visited and grid[newr][newc] == 1:
                        visited.add((newr,newc))
                        area += 1
                        q.append((newr,newc))
            
            return area+1


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    visited.add((r,c))
                    res = max(res, bfs(r,c))
        return res