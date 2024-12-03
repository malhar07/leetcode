class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]

        if color == "B":
            opp = "W"
        else:
            opp = "B"
        
        for dr,dc in directions:
            r,c = rMove+dr, cMove+dc
            count=1
            # if 0<=r<8 and 0<=c<8 and board[r][c] == opp:
            while 0<=r<8 and 0<=c<8:
                if board[r][c] == ".":
                    break
                if board[r][c] == opp:
                    count+=1
                    # continue
                if board[r][c] == color:
                    if count>=2:
                        return True
                    break
                r+=dr
                c+=dc
        print(count)
        return False

# ["W","W",".","B",".","B","B","."],
# ["W","B",".",".","W","B",".","."],
# ["B","B","B","B","W","W","B","."],
# ["W","B",".",".","B","B","B","."],
# ["W","W","B",".","W",".","B","B"],
# ["B",".","B","W",".","B",".","."],
# [".","B","B","W","B","B",".","."],
# ["B","B","W",".",".","B",".","."]]