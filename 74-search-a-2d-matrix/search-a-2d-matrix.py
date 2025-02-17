class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = len(matrix)
        w = len(matrix[0])

        left = 0
        right = l*w - 1

        while left <= right:
            mid = (left+right)//2

            row, col = mid//w, mid%w

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid+1
            else:
                right = mid-1
        return False