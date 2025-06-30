class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        visited = set()
        def dfs(r,c):
            visited.add((r,c))
            found = True
            if grid1[r][c] != 1:
                found = False
            # found = grid1[r][c] == 1

            for dr, dc in dirs:
                newr, newc = r+dr, c+dc
                if 0<=newr<len(grid2) and 0<=newc<len(grid2[0]) and (newr,newc) not in visited and grid2[newr][newc] == 1:
                    # visited.add((newr,newc))
                    found =  dfs(newr,newc) and found
            return found

        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i,j) not in visited:
                    
                    if dfs(i,j):
                        print(i, " ", j)
                        count+=1
        return count

# class Solution:
#     def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
#         dirs = [(0,1), (1,0), (-1,0), (0,-1)]
#         visited = set()

#         def dfs(r, c):
#             visited.add((r, c))
#             is_sub = grid1[r][c] == 1
#             for dr, dc in dirs:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < len(grid2) and 0 <= nc < len(grid2[0]) and grid2[nr][nc] == 1 and (nr, nc) not in visited:
#                     is_sub = dfs(nr, nc) and is_sub
#             return is_sub

#         count = 0
#         for i in range(len(grid2)):
#             for j in range(len(grid2[0])):
#                 if grid2[i][j] == 1 and (i, j) not in visited:
#                     if dfs(i, j):
#                         count += 1
#         return count
