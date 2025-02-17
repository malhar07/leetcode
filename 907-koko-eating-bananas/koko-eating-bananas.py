class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = -1

        while left <= right:
            mid = (left+right)//2
            time = 0
            for p in piles:
                time+=(p-1)//mid + 1
            if time <= h:
                right = mid-1
                res = mid
            else:
                left = mid+1
        return res