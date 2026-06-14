class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        res = sum(weights)
        while low <= high:
            print(low + (high-low)//2)
            mid = low + (high-low)//2
            curr_weight = 0
            ships = 1
            for w in weights:
                if w+curr_weight > mid:
                    ships+=1
                    curr_weight = 0
                curr_weight += w
            if ships <= days:

                res = min(res, mid)
                high = mid-1
            else:
                low = mid+1
        return res