class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        squares.sort(key = lambda x: x[1])
        total_area = 0
        top_most = 0
        for sq in squares:
            top_most = max(top_most,sq[1]+sq[2])

            total_area+=sq[2]**2
        right = top_most
        left = squares[0][1]

        while right-left>1e-5:
            
            mid = left + (right-left)/2
            curr_area = 0
            ind = 0
            # print(mid)
            while ind < len(squares) and squares[ind][1]<mid:
                ratio = min(1,( mid - squares[ind][1])/squares[ind][2])
                curr_area += (squares[ind][2]**2)*ratio
                ind+=1
            if abs(curr_area - total_area/2) < 1e-5:
                right = mid
            elif curr_area < total_area/2:
                left = mid
            else:
                right = mid
        return (left+right)/2