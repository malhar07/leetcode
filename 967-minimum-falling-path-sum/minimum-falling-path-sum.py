class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = {}

        def helper(row, col):
            if row == n:
                return 0
            if (row,col) in dp:
                return dp[(row,col)]
            if col>0:
                left = helper(row+1, col-1)
            else:
                left =  math.inf
            mid = helper(row+1, col)
            if col<n-1:
                right = helper(row+1,col+1)
            else:
                right =  math.inf

            dp[(row,col)] = min(left,mid,right)+matrix[row][col]
            return min(left,mid,right)+matrix[row][col]

        res = math.inf
        for i in range(n):
            res = min(res,helper(0,i))
        return res