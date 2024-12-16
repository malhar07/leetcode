class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.arr = []

        heapq.heapify(self.arr)

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:

        if len(self.arr)<self.k:
            heapq.heappush(self.arr, val)
        else:
            num = heapq.heappop(self.arr)
            heapq.heappush(self.arr, max(num, val))
        return self.arr[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)