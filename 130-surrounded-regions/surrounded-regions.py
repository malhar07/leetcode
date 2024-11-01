class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row, col = len(board), len(board[0])
        visited = set()
        
        # self.flag = False

        def bfs(r,c):
            path = set()
            flag = False
            q = deque()
            q.append((r,c))
            path.add((r,c))
            print(path)
            visited.add((r,c))

            

            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    if r in [0, row-1] or c in [0, col-1]:
                        flag = True

                    directions = [[-1,0], [1,0], [0,-1], [0,1]]
                    for dr, dc in directions:
                        if r+dr < 0 or r+dr >=len(board) or c+dc < 0 or c+dc >= len(board[0]) or (r+dr,c+dc) in path or board[r+dr][c+dc]!="O":
                            continue
                        q.append((r+dr, c+dc))
                        path.add((r+dr,c+dc))
                        visited.add((r+dr,c+dc))

            if flag == False:
                for r,c in path:
                    board[r][c] = "X"
            
            
            

        for r in range(row):
            for c in range(col):
                if (r,c) not in visited and board[r][c] == "O":
                    bfs(r,c)
        