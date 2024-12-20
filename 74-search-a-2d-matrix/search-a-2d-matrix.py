class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left = 0
        right = (m*n)-1
        print(m, " ", n)

        while left<= right:
            mid = (left+right)//2
            row = mid//n
            col = mid%n
            print(mid)
            print(row, " ", col)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid-1
            else:
                left = mid+1
        return False