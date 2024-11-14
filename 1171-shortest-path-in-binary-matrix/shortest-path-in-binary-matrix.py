class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        

        def bfs():
            q = deque()
            visited = set()

            q.append((0,0,1))
            visited.add((0,0))
            directions = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]
            while q:
                for i in range(len(q)):
                    r,c, moves = q.popleft()
                    print(r," ", c)
                    if r == len(grid)-1 and c == len(grid)-1:
                        return moves
                    for dr, dc in directions:
                        if 0<=r+dr<len(grid) and 0<=c+dc<len(grid) and (r+dr, c+dc) not in visited and grid[r+dr][c+dc] == 0:
                            # print(r+dr, " ", c+dc)
                            q.append((r+dr, c+dc, moves+1))
                            visited.add((r+dr, c+dc))
            return -1
        
        if grid[0][0]!= 0:
            print(".vevev")
            return -1
        return bfs()
                
