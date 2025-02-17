class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        right = sum(weights)
        left = max(weights)

        while left <= right:
            mid = (left+right)//2
            print(mid)

            total = 0
            d = 1
            for w in weights:
                if total+w > mid:
                    d+=1
                    total = 0
                total+=w
            if d <=days:
                res = mid
                right = mid-1
            else:
                left = mid+1
        return res

