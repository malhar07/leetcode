class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        heap = []
        pos = 0
        for num, frm, to in trips:
            while heap and heap[0][0] <= frm:
                curr = heapq.heappop(heap)
                capacity += curr[1]
            if num> capacity:
                return False
            else:
                capacity-=num
            heapq.heappush(heap,[to,num])
        return True

             