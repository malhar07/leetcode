class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = len(intervals)
        print(count)
        intervals.sort()
        curr = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0] == curr[0]:
                if curr[1] <= intervals[i][1]:
                    count-=1
                # else:
                curr = intervals[i]
            else:
                if intervals[i][0] < curr[1] and intervals[i][1] <= curr[1]:
                    count-=1
                else:
                    curr = intervals[i]
        return count



        # [1,5] [2,8] [3,4]