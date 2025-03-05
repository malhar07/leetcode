class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 1

        heap = []
        heapq.heappush(heap,intervals[0][1])

        for i in range(1, len(intervals)):
            if intervals[i][0] < heap[0]:
                # heapq.heappush(hep, intervals[i][1])
                res = max(res, len(heap)+1)
            else:
                while heap and heap[0] <= intervals[i][0]:
                    heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])
        return res