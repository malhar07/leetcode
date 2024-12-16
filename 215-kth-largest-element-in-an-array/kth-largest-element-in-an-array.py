class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minH = []
        heapq.heapify(minH)

        for i in nums:
            if len(minH) < k:
                heapq.heappush(minH, i)
            else:
                if i > minH[0]:
                    heapq.heappop(minH)
                    heapq.heappush(minH, i)
        return minH[0]