class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dim = [len(matrix), len(matrix[0])]

        top = 0
        bottom = len(matrix)-1
        right = len(matrix[0])-1
        left = 0
        res = []

        while top <= bottom and left <= right:
            
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top+=1
            
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right-=1
            if top <= bottom and left <= right:

                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left+=1
        return res