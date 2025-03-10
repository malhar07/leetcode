class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        res = 0

        def bfs(r,c):
            flag = True
            q = deque([(r,c)])
            directions = [[0,1],[1,0],[0,-1],[-1,0]]

            visited.add((r,c))
            if grid1[r][c] != 1:
                flag = False

            while q:
                r,c = q.popleft()
                for dr, dc in directions:
                    newr, newc = r+dr, c+dc

                    if 0<=newr<len(grid2) and 0<=newc<len(grid2[0]) and (newr,newc) not in visited and grid2[newr][newc] == 1:
                        if grid1[newr][newc] == 0:
                            flag = False
                        # else:

                        q.append((newr,newc))
                        visited.add((newr,newc))
            return flag


        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i,j) not in visited:# and grid1[i][j]==1:
                    if bfs(i,j):
                        print(i, " ",j)
                        res+=1
        return res
                

#
[[1,1,1,1,0,1],[0,0,1,0,1,0],[1,1,1,1,1,1],[0,1,1,1,1,1],[1,1,1,0,1,0],[0,1,1,1,1,1],[1,1,0,1,1,1],[1,0,0,1,0,1],[1,1,1,1,1,1],[1,0,0,1,0,0]]