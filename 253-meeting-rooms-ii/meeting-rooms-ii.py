class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intervals.sort()
        # res = 1

        # heap = []
        # heapq.heappush(heap,intervals[0][1])

        # for i in range(1, len(intervals)):
        #     if intervals[i][0] < heap[0]:
        #         res = max(res, len(heap)+1)
        #     else:
        #         while heap and heap[0] <= intervals[i][0]:
        #             heapq.heappop(heap)
        #     heapq.heappush(heap, intervals[i][1])
        # return res

        # intervals.sort()

        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        s,e = 0,0
        count, res = 0,0

        while s < len(start):
            if start[s] < end[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            res = max(res,count)
        return res