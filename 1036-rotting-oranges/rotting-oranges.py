class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        count = 0
        time = 0
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    count+=1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr, dc in dirs:
                    newr, newc = r+dr, c+dc

                    if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and grid[newr][newc] == 1:
                        grid[newr][newc] = 2
                        q.append((newr,newc))
                        count-=1
            time+=1
        if count > 0:
            return -1
        else:
            if time == 0:
                return time
            else:
                return time-1
        


