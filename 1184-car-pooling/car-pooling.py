class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = []
        trips.sort(key = lambda x: x[1])
        print(trips)
        print(capacity)

        for p, f, t in trips:
            while len(arr)>0 and arr[0][0] <= f:
                tp = heapq.heappop(arr)
                capacity+=tp[1]
            if capacity >= p:
                capacity-=p
                print([t,p])
                heapq.heappush(arr, [t, p])
            else:
                return False
        return True