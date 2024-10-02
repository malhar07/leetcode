class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        curr = 0
        res = right + 1

        while left <= right:
            mid = (left + right)//2
            curr = 0

            for i in piles:
                curr += (i + mid-1) // mid
            if curr <= h:
                right = mid - 1
                res = min(res, mid)
                # print(curr, " ", mid)
            else:
                left = mid + 1
            
            # print(mid)
            
        return res