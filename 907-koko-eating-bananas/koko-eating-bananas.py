class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = max(piles)

        while left <= right:
            mid = left + (right-left)//2

            hours = sum([math.ceil(i/mid) for i in piles])
            print(hours)

            if hours <= h:
                res = min(mid, res)
                right = mid-1
                
            else:
                left = mid+1
        return res