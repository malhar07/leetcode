class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = deque()
        visited = set()
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        for r in range(len(board)):
            if board[r][0] == "O":
                q.append((r,0))
                visited.add((r,0))
            if board[r][-1] == "O":
                q.append((r,len(board[0])-1))
                visited.add((r,len(board[0])-1))
            
        for c in range(len(board[0])):
            if board[0][c] == "O":
                q.append((0,c))
                visited.add((0,c))
            if board[-1][c] == "O":
                q.append((len(board)-1,c))
                visited.add((len(board)-1,c))
        
        def bfs(q):

            while q:
                r,c = q.popleft()
                board[r][c] = "M"

                for dr, dc in directions:
                    newr, newc = r+dr, c+dc
                    if 0<=newr<len(board) and 0<=newc<len(board[0]) and (newr, newc) not in visited and board[newr][newc] == "O":
                        q.append((newr,newc))
                        visited.add((newr, newc))

        bfs(q)
        print(board)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "M":
                    board[r][c] = "O"
        


        # ["X","X","X","X","O"],
        # ["X","O","O","X","X"],
        # ["O","X","X","X","X"]]

        # ["X","X","O","X","O"]
        # ["X","O","O","X","X"]
        # ["O","X","X","X","X"]]