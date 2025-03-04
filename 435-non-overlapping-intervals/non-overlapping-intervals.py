class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        arr = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] < arr[-1][1]:
                count+=1
                arr[-1][1] = min(arr[-1][1], intervals[i][1])
            else:
                arr.append(intervals[i])
        return count