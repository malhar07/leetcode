class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        rows, cols = len(grid2), len(grid2[0])
        subIslands = 0

        def bfs(row,col):
            q = deque()
            q.append((row,col))
            valid = True

            while q:
                (r,c) = q.popleft()   
                if grid1[r][c] != 1:
                    valid = False
                
                for dr, dc in directions:
                    newr, newc = r+dr, c+dc

                    if 0<=newr<rows and 0<=newc<cols and grid2[newr][newc] == 1 and (newr, newc) not in visited:
                        q.append((newr, newc))
                        visited.add((newr, newc))
            if not valid:
                return 0
            return 1


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid2[r][c] == 1:
                    visited.add((r,c))
                    subIslands += bfs(r,c)
        return subIslands