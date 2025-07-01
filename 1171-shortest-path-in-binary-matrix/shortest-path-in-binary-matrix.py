class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        visited = set()

        if grid[0][0]!= 0 :
            return -1

        q.append((0,0,1))
        visited.add((0,0))
        directions = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]
        while q:
            for _ in range(len(q)):
                r,c,path_len = q.popleft()
                if r == n-1 and c == n-1:
                    return path_len

                for dr, dc in directions:
                    newr, newc = r+dr, c+dc
                    if 0<=newr<n and 0<=newc<n and (newr,newc) not in visited and grid[newr][newc]==0:
                        # if newr == n-1 and newc == n-1:
                        #     return path_len+1
                        visited.add((newr,newc))
                        q.append((newr,newc,path_len+1))
        return -1