class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        row = len(board)
        col = len(board[0])
        visited = set()
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr, dc in directions:
                        newr = r+dr
                        newc = c+dc
                        if 0<=newr<row and 0<=newc<col and board[newr][newc] == "X" and (newr,newc) not in visited:
                            visited.add((newr,newc))
                            q.append((newr,newc))
        def check(r,c):
            if (r-1 < 0 or board[r-1][c] == ".") and (c-1<0 or board[r][c-1]=="."):
                return True
            return False
            
            
        
        for i in range(row):
            for j in range(col):
                print(i, " ", j)
                if board[i][j] == 'X' and (i,j) not in visited:
                    # bfs(i,j)
                    count+=check(i,j)
                    # count+=1
        return count