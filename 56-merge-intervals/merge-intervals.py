class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        ind = 0
        while ind < len(intervals):
            s,e = intervals[ind]
            ind+=1
            while ind < len(intervals) and e >= intervals[ind][0]:
                e = max(intervals[ind][1], e)
                ind+=1
            res.append([s,e])
        return res
