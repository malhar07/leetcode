class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_set, col_set = set(), set()
        for i in range(rows):
            count = 0
            for j in range(cols):
                if grid[i][j] == 1:
                    count+=1
                if count >= 2:
                    row_set.add(i)
        for j in range(cols):
            count = 0
            for i in range(rows):
                if grid[i][j] == 1:
                    count+=1
                if count >= 2:
                    col_set.add(j)
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i in row_set or j in col_set):
                    count+=1
        return count