class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                grid_num = 3*(i//3) + (j//3)
                if board[i][j]!='.':
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in grid[grid_num]:
                        return False
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    grid[grid_num].add(board[i][j])
        return True