class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        res = -1
        while low<=high:
            mid = low + (high-low)//2
            count = 1
            curr_weight = 0
            for w in weights:
                if curr_weight + w > mid:
                    count+=1
                    curr_weight = 0
                curr_weight += w
            if count<=days:
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res