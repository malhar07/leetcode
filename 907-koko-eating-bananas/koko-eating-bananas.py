class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high-low)//2

            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            
            if time <= h:
                res = min(res,mid)
                high = mid-1
            else:
                    low = mid+1
        return res