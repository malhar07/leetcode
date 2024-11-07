class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        path = set()
        # self.length = len(word)
        self.found = False

        def dfs(r,c, ind):

            # if
            # print(board[r][c])

            if board[r][c] != word[ind]:
                path.remove((r,c))
                return False
            else:
                # if ind == self.length-1:
                if ind == len(word)-1:
                    print("word Found")
                    self.found = True
                    return True
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    if 0<= r+dr < len(board) and 0<= c+dc < len(board[0]) and (r+dr, c+dc) not in path:
                        path.add((r+dr,c+dc))
                        dfs(r+dr, c+dc, ind+1)
                path.remove((r,c))
                
                return False


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    path = set()
                    path.add((row, col))
                    dfs(row, col, 0)
                    # path.remove((row,col))
                    # if dfs(row,col, 0):
                    #     return True
        return self.found
        # return False