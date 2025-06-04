class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for i in range(len(nums)):
            if len(self.heap)<k:
                heapq.heappush(self.heap,nums[i])
            else:
                if self.heap[0] < nums[i]:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, nums[i])


    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
            return self.heap[0]
        if self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)     
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)