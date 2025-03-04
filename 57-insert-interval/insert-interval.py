class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        ind = 0
        while ind < len(intervals) and intervals[ind][0] <= newInterval[0]:
            res.append(intervals[ind])
            ind+=1
        if ind>0 and newInterval[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], newInterval[1])
        else:
            res.append(newInterval)
        
        for i in range(ind, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res
        