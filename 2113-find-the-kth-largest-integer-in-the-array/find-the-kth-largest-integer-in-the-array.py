class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr = []

        for num in nums:
            heapq.heappush(arr, int(num))
            if len(arr)>k:
                heapq.heappop(arr)
        return str(heapq.heappop(arr))