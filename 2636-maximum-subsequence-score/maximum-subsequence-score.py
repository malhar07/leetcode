class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = []
        for n1,n2 in zip(nums1,nums2):
            arr.append((n1,n2))
        arr.sort(key = lambda x: x[1], reverse = True)
        _sum = 0
        res = 0
        heap = []
        for n1,n2 in arr:
            _sum+=n1
            heapq.heappush(heap,n1)

            if len(heap)>k:
                temp = heapq.heappop(heap)
                _sum-=temp
            if len(heap) == k:
                res = max(res, _sum*n2)
        return res
            

        # pairs = sorted(zip(nums1, nums2), key=lambda p: p[1], reverse=True)

        # minHeap = []
        # n1Sum = 0
        # res = 0

        # for n1, n2 in pairs:
        #     n1Sum += n1
        #     heapq.heappush(minHeap, n1)

        #     if len(minHeap) > k:
        #         n1Sum -= heapq.heappop(minHeap)

        #     if len(minHeap) == k:
        #         res = max(res, n1Sum * n2)

        # return res
