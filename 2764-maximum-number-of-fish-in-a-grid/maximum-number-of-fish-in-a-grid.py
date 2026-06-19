class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        max_fish = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        visited = set()

        def bfs(row, col):
            q=deque()
            q.append((row, col))
            curr_fish = 0

            while q:
                r,c = q.popleft()
                curr_fish+=grid[r][c]

                for dr, dc in directions:
                    newr, newc = r+dr, c+dc

                    if 0<=newr<rows and 0<=newc<cols and (newr,newc) not in visited and grid[newr][newc] > 0:
                        q.append((newr, newc))
                        visited.add((newr,newc))
            return curr_fish
                    



        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0 and (r,c) not in visited:
                    visited.add((r,c))
                    max_fish = max(max_fish, bfs(r,c))
        return max_fish