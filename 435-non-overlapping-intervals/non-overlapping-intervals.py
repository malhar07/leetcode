class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 0
        last_end_time = -math.inf

        for start, end in intervals:
            if start < last_end_time:
                count+=1
                #overlap
            else:
                last_end_time = end
        return count

        # arr = [intervals[0]]
        # for i in range(1,len(intervals)):
        #     if intervals[i][0] < intervals[i-1][1]:
        #         count+=1
        #         intervals[i-1][1] = min(intervals[-1][1], intervals[i][1])
        #         skip = True
        #     # else:
        #     #     arr.append(intervals[i])
        # return count