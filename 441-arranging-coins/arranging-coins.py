class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = (n//2 )+1
        res = 1
        while left <= right:
            mid = (left+right)//2
            if (mid*(mid+1))//2 == n:
                return mid
            elif (mid*(mid+1))//2 < n:
                res = mid
                left = mid+1
            else:
                right = mid-1
        return res


        