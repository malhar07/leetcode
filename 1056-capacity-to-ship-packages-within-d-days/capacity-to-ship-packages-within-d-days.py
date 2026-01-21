class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def get_days(capacity):
            ships = 0
            curr_weight = 0

            for w in weights:
                if curr_weight + w > capacity:
                    ships += 1
                    curr_weight = 0
                curr_weight += w
            return ships+1


        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = left + (right-left)//2

            total_days = get_days(mid)

            if total_days <= days:
                res = mid
                right = mid-1
            else:
                left = mid+1
        return res