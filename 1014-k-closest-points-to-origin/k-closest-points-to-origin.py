class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heap = [((p[0]**2 + p[1]**2)*-1, p[0], p[1]) for p in points]
        # heapq.heapify(heap)
        # while len(heap) > k:
        #     heapq.heappop(heap)
        # return [[p[1], p[2]] for p in heap]
        heap = []
        for x, y in points:

            dist = x**2 + y**2

            heapq.heappush(heap, (-dist,x,y))

            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for dist, x, y in heap]