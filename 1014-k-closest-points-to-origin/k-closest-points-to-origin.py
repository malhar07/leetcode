class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap =[]
        res = []
        for x,y in points[:k]:
            heapq.heappush(heap, [(x**2+y**2)*-1, x, y])
        for x,y in points[k:]:
            curr = (x**2+y**2)*-1
            if heap[0][0] < curr:
                heapq.heappop(heap)
                heapq.heappush(heap, [curr, x, y])

        while heap:
            res.append(heapq.heappop(heap)[1:])
        return res
