class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = copy.deepcopy(matrix)



        for i in range(len(self.prefix)):
            for j in range(1, len(self.prefix[0])):
                self.prefix[i][j] += self.prefix[i][j-1]
        print(self.prefix)
        for j in range(len(self.prefix[0])):
            for i in range(1, len(self.prefix)):
                self.prefix[i][j] += self.prefix[i-1][j]

        print(self.prefix)
        




    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col1 > 0:
            left = self.prefix[row2][col1-1]
        else:
            left = 0
        if row1>0:
            up = self.prefix[row1-1][col2]
        else:
            up = 0
        if row1>0 and col1>0:
            corner = self.prefix[row1-1][col1-1]
        else:
            corner = 0
        total = self.prefix[row2][col2] - left - up + corner
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)