class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        res = 0
        for i in range(k):
            if i < len(nums):
                heap.append(nums[i])
            else:
                break
        heapq.heapify(heap)
        for i in nums[k:]:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
        
        for i in range(len(heap)):
            heap[i] = -heap[i]
        heapq.heapify(heap)
        # print(heap)
        
        for i in range(k):
            # print(heap)
            x = heapq.heappop(heap)
            res+= -x
            heapq.heappush(heap, math.ceil((-x)/3)*-1)
            # heap[0] = (heap[0]-2)//3
        return res