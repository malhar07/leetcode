class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = [[frm, to, num] for num, frm, to in trips]
        heapq.heapify(heap)

        curr_seats = 0
        curr_dist = 0
        passengers = [] #to, from, num
        while True:
            # curr_dist = heap[0][0]
            if not heap:
                break
            else:
                curr_dist = heap[0][0]

            while passengers and passengers[0][0] <= curr_dist:
                t2, f2, n2 = heapq.heappop(passengers)
                curr_seats-=n2

            while heap and heap[0][0] == curr_dist:
                f, t, n = heapq.heappop(heap)
                curr_seats += n
                heapq.heappush(passengers, [t, f, n])

                if curr_seats > capacity:
                    return False
        return True
                
