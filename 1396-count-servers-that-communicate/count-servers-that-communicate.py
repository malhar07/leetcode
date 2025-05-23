class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        connected = set()

        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            arr = []
            for j in range(col):
                if grid[i][j] == 1:
                    arr.append((i,j))
            if len(arr) > 1:
                connected.update(arr)

        for j in range(col):
            arr = []
            for i in range(row):
                if grid[i][j] == 1:
                    arr.append((i,j))
            if len(arr)>1:
                connected.update(arr)
        return len(connected)

