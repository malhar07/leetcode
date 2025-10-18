class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix) + 1
        cols = (len(matrix[0]) if matrix else 0) + 1
        self.new_mat = [[0] * cols for _ in range(rows)]

        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                self.new_mat[i][j] = matrix[i][j]+self.new_mat[i][j+1]+self.new_mat[i+1][j]-self.new_mat[i+1][j+1]
        print(self.new_mat)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.new_mat[row1][col1]-self.new_mat[row2+1][col1]-self.new_mat[row1][col2+1]+self.new_mat[row2+1][col2+1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

[[58, 44, 35, 28, 20, 0], 
[48, 37, 28, 22, 18, 0], 
[31, 25, 22, 19, 17, 0], 
[22, 17, 16, 13, 12, 0], 
[9,  8,  8,  5,  5,  0], 
[0,  0,  0,  0,  0,  0]]