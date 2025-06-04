class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = 0
        right = len(intervals)-1


        while left<= right:
            mid = left + (right-left)//2

            if intervals[mid][0] >= newInterval[0]:
                right = mid-1
            else:
                left = mid+1
                
        
        intervals.insert(left, newInterval)
        res = []
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
                
        return res