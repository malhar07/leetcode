class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        row = len(board)
        col = len(board[0])
        
        def check(r,c):
            if (r-1 < 0 or board[r-1][c] == ".") and (c-1<0 or board[r][c-1]=="."):
                return True
            return False
            
    
    #traverse the board once, chceck if the "X" is top left "X" of the ship.
        
        for i in range(row):
            for j in range(col):

                if board[i][j] == 'X':
                    count+=check(i,j)
        return count