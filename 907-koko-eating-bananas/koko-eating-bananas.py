class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = sum(piles)

        while left <= right:
            print(left, " ", right)
            time = 0
            mid = left+(right-left)//2
            for num in piles:
                time+=math.ceil(num/mid)
            if time > h:
                left = mid+1
            else:
                res = mid
                right = mid-1
            
        return res
