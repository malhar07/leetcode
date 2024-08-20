class Solution:
    def arrangeCoins(self, n: int) -> int:

        left = 0
        right = n

        while left <= right:
            mid = (left+right)//2
            if ((mid)*(mid+1))/2 > n:
                right = mid-1
            else:
                left = mid+1
        return right
        