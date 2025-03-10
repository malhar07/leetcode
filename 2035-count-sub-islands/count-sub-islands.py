class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        res = 0
        self.flag = True

        def bfs(r,c):
            directions = [[0,1],[1,0],[0,-1],[-1,0]]

            # visited.add((r,c))

            for dr, dc in directions:
                newr, newc = r+dr, c+dc

                if 0<=newr<len(grid2) and 0<=newc<len(grid2[0]) and (newr,newc) not in visited and grid2[newr][newc] == 1:
                    if grid1[newr][newc] == 0:
                        self.flag = False
                    visited.add((newr,newc))
                    bfs(newr,newc)
                    
            return self.flag

            # flag = True
            # q = deque([(r,c)])
            # directions = [[0,1],[1,0],[0,-1],[-1,0]]

            # visited.add((r,c))

            # while q:
            #     r,c = q.popleft()
            #     for dr, dc in directions:
            #         newr, newc = r+dr, c+dc

            #         if 0<=newr<len(grid2) and 0<=newc<len(grid2[0]) and (newr,newc) not in visited and grid2[newr][newc] == 1:
            #             if grid1[newr][newc] == 0:
            #                 flag = False

            #             q.append((newr,newc))
            #             visited.add((newr,newc))
            # return flag


        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i,j) not in visited:
                    self.flag = True
                    visited.add((i,j))
                    flag = bfs(i,j)
                    if flag and grid1[i][j]==1:
                        res+=1
                        
        return res