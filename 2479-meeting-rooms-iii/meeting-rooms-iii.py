# class Solution:
#     def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
#         meetings.sort()
#         res = [0]*n
#         open_rooms = [i for i in range(n)]
#         ongoing_meetings = []
#         heapq.heapify(open_rooms)

#         for meet in meetings:
#             curr_time = meet[0]
#             if len(open_rooms) == 0 and ongoing_meetings and curr_time < ongoing_meetings[0][0]:
#                 curr_time = ongoing_meetings[0][0]

#             while ongoing_meetings and ongoing_meetings[0][0]<= curr_time:
#                 free_room = heapq.heappop(ongoing_meetings)[1]
#                 heapq.heappush(open_rooms, free_room)
            
#             room = heapq.heappop(open_rooms)
#             res[room]+=1
#             curr_meeting = [meet[1] + curr_time-meet[0], room]
#             heapq.heappush(ongoing_meetings,curr_meeting)
#         room,result = -1,0
#         print(res)
#         for ind, count in enumerate(res):
#             if count > result:
#                 result = count
#                 room = ind
#         return room

import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res = [0] * n
        open_rooms = list(range(n))
        ongoing_meetings = []
        heapq.heapify(open_rooms)

        for start, end in meetings:
            # Free up any rooms that are done before the current meeting starts
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                _, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(open_rooms, room)
            
            # Assign room
            if open_rooms:
                room = heapq.heappop(open_rooms)
                heapq.heappush(ongoing_meetings, (end, room))
            else:
                # Delay meeting to the earliest room free time
                earliest_end, room = heapq.heappop(ongoing_meetings)
                duration = end - start
                heapq.heappush(ongoing_meetings, (earliest_end + duration, room))
            res[room] += 1

        # Find room with max usage
        max_count = max(res)
        for i in range(n):
            if res[i] == max_count:
                return i



        