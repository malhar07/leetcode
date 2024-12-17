class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # arr = []
        # trips.sort(key = lambda x: x[1])

        # for p, f, t in trips:
        #     while len(arr)>0 and arr[0][0] <= f:
        #         tp = heapq.heappop(arr)
        #         capacity+=tp[1]
        #     if capacity >= p:
        #         capacity-=p
        #         heapq.heappush(arr, [t, p])
        #     else:
        #         return False
        # return True
        trips.sort(key = lambda x: x[1])
        arr = []
        for i in range(len(trips)):
            current_time = trips[i][1]
            while len(arr)>0 and arr[0][0] <= current_time:
                t, np = heapq.heappop(arr)
                capacity += np
            if trips[i][0] <= capacity:
                capacity-=trips[i][0]
                heapq.heappush(arr, [trips[i][2], trips[i][0]])
            else:
                return False
        return True