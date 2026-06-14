class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        left = 1
        right = x//2
        res = 0

        while left <= right:

            mid = left + (right-left)//2

            if mid**2 < x:
                res = max(res, mid)
                left = mid+1
            elif mid**2 > x:
                right = mid-1
            else:
                return mid
        return res