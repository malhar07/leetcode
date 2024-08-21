class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        res = right

        day_count = 0

        while left <= right:
            mid = left + (right-left)//2

            day_count = 1
            curr_weight = 0

            for i in weights:
                if curr_weight + i <= mid:
                    curr_weight += i
                    
                else:
                    day_count += 1
                    curr_weight = i
                
                if day_count > days:
                    break
            
            print(day_count, " ", mid)

            if day_count > days:
                left = mid+1
            else:
                right = mid-1
                res = min(mid,res)
        return res
