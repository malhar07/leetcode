class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(k):
            heapq.heappush(heap, nums[i])
        
        # heapq.heapify(heap)

        for i in nums[k:]:
            if i > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
                # heapq.heapify(heap)
        
        return heap[0]