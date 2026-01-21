class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def count_hours(speed):
            return sum([math.ceil(x/speed) for x in piles])
        left = 1
        right = max(piles)

        while left <= right:
            mid = left + (right-left)//2

            time = count_hours(mid)

            if time <= h:
                res = mid
                right = mid-1
            elif time > h:
                left = mid+1
        return res