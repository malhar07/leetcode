class SeatManager:

    def __init__(self, n: int):
        self.curr_seat = 1
        self.arr = []

    def reserve(self) -> int:
        if self.arr:
            return heapq.heappop(self.arr)
        
        self.curr_seat+=1
        return self.curr_seat-1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.arr, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)