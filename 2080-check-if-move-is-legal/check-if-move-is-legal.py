class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        mid_color = "W" if color == "B" else "B"
        dirs = [[-1,0], [0,-1], [1,0], [0,1], [-1,-1], [-1,1], [1,1], [1,-1]]

        def check_mid(dr, dc, mid_color):
            print(dr, " ", dc)
            count = 0
            newr, newc = rMove+dr, cMove+dc
            while 0<=newr<len(board) and 0<=newc<len(board[0]) and board[newr][newc] == mid_color:  
                print(board[newr][newc])
                newr += dr
                newc+=dc
                count+=1
            if count > 0 and 0<=newr<len(board) and 0<=newc<len(board[0]) and board[newr][newc] == color:
                return True
            return False
        
        for dr, dc in dirs:
            if check_mid(dr,dc, mid_color):
                return True
        return False


# ["B","W","B","B","W","W",".","W"],
# ["W","W","B","W","B","B","W","."],
# ["B","W",".","W",".",".","B","B"],
# [".","B","W",".","B","W","B","W"],
# ["B","B","W","B",".","B","W","B"],
# ["B","B","B","W","B","W","W","B"],
# [".","W",".","W",".","W","W","W"],
# [".","W","W","B","B","B","B","."]]