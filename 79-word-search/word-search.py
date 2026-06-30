class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        rows, cols = len(board), len(board[0])
        visited = set()

        def checkNextChar(row, col, ind):
            if row < 0 or row>= len(board) or col < 0 or col >= len(board[0]):
                return False
            if (row, col) in visited:
                return False
            if board[row][col] != word[ind]:
                return False
            return True
            

        def backtrack(r,c,i):
            if i == len(word)-1:
                return True
            visited.add((r,c))


            for dr, dc in directions:
                newr, newc = r+dr, c+dc
                if checkNextChar(newr, newc, i+1):
                    if backtrack(newr, newc, i+1):
                        return True

            visited.remove((r,c))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(r,c,0):
                        return True
        return False


        ["C","A","A"]
        ["A","A","A"]
        ["B","C","D"]