class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # self.nums = nums
        self.arr = []

        for num in nums:
            self.add(num)

        # heapq.heapify(self.arr)
        # for i in range(self.k):
        #     if i < len(self.nums):
        #         self.arr.append(self.nums[i])
        # for i in range(k,len(self.nums)):
        #     if self.nums[i] > self.arr[0]:
        #         heapq.heappop(self.arr)
        #         heapq.heappush(self.arr, self.nums[i])

    def add(self, val: int) -> int:
        if len(self.arr) < self.k:
            heapq.heappush(self.arr, val)
        elif val > self.arr[0]:
            heapq.heappop(self.arr)
            heapq.heappush(self.arr, val)
        return self.arr[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)