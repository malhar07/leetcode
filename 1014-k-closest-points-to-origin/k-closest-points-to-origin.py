class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for x, y in points:
            d = x**2 + y**2
            dist.append([d, x, y])
        
        heapq.heapify(dist)
        res = []
        for i in range(k):
            d,x,y = heapq.heappop(dist)
            res.append([x,y])
        return res