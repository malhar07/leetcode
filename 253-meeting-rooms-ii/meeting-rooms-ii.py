class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [intervals[0][1]]
        res = 1
        count = 1

        for i in range(1,len(intervals)):
            while heap and intervals[i][0] >= heap[0]:
                count-=1
                heapq.heappop(heap)
            # if heap:
            count+=1
            res = max(res,count)
            heapq.heappush(heap, intervals[i][1])
      
        return max(res,count)
