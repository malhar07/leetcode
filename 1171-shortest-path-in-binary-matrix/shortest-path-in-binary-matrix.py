class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def checkValidCell(row, col):
            if row<0 or row>=n:
                return False
            if col < 0 or col>=n:
                return False
            if grid[row][col] == 1:
                return False
            return True

        n = len(grid)
        directions = [[0,1], [0,-1], [-1,-1], [-1,0], [-1,1], [1,-1], [1,0], [1,1]]
        res = 1
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        q = deque([(0,0,1)])
        grid[0][0] = 1

        while q:
            r,c,count = q.popleft()
            
            if r == n-1 and c == n-1:
                    return count

            for dr, dc in directions:
                newr, newc = r+dr, c+dc
                if checkValidCell(newr, newc):
                    q.append((newr,newc,count+1))
                    grid[newr][newc] = 1

        return -1