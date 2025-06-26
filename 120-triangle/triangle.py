class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def helper(row, col):
            if row == len(triangle):
                return 0
            if (row,col) not in memo:
                memo[(row,col)] = min(helper(row+1,col), helper(row+1, col+1)) + triangle[row][col]
            return memo[(row,col)]
        return helper(0,0)