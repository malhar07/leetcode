class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def dfs(r,c):
            visited.add((r,c))

            directions = [[-1,0], [1,0], [0,-1], [0,1]]
            for dr, dc in directions:
                    if r+dr < 0 or r+dr >=len(grid) or c+dc < 0 or c+dc >= len(grid[0]) or (r+dr,c+dc) in visited or grid[r+dr][c+dc]!="1":
                        continue
                    visited.add((r+dr,c+dc))
                    dfs(r+dr, c+dc)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == "1":
                    # print(visited)
                    dfs(r,c)
                    islands+=1
        return islands
        