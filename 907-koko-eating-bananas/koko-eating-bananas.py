class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = max(piles)

        while left <= right:
            
            hours = 0
            mid = (left+right) // 2
            for i in piles:
                hours += ((i-1) // mid)+1
            # print(left, " ", right, " ", hours)
            if hours <= h:
                res = min(res, mid)
                right = mid-1
            else:
                left = mid+1
        return res
            
            