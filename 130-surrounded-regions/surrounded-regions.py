class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        que = deque()
        rows, cols = len(board), len(board[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]

        for i in range(rows):
            if board[i][0] == "O":
                que.append((i,0))
            if board[i][cols-1] == "O":
                que.append((i, cols-1))
        for i in range(1,cols):
            if board[0][i] == "O":
                que.append((0,i))
            if board[rows-1][i] == "O":
                que.append((rows-1,i))
        
        def bfs(que):
            visited = set()

            visited.update(que)

            while que:
                r,c = que.popleft()

                for dr, dc in dirs:
                    newr, newc = r+dr, c+dc

                    if 0<=newr<rows and 0<=newc<cols and (newr,newc) not in visited and board[newr][newc]=="O":
                        que.append((newr,newc))
                        visited.add((newr,newc))
            return visited
        visited = bfs(que)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i,j) not in visited:
                    print("kkkk")
                    board[i][j] = "X"
        

        