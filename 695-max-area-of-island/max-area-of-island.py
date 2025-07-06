class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]

        visited = set()

        max_area = 0

        def bfs(r,c):
            area = 0
            q = deque([(r,c)])
            visited.add((r,c))
            while q:
                r,c = q.popleft()
                area+=1

                for dr, dc in dirs:
                    newr, newc = r+dr, c+dc

                    if 0<=newr<rows and 0<=newc<cols and (newr, newc) not in visited and grid[newr][newc] == 1:
                        visited.add((newr,newc))
                        q.append((newr,newc))
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area, bfs(r,c))
        return max_area
            