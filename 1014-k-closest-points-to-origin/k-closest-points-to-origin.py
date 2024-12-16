class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        heapq.heapify(dist)
        for x, y in points:
            d = -(x**2 + y**2)
            # dist.append([d, x, y])

            if len(dist) < k:
                heapq.heappush(dist, [d, x, y])
            else:
                if d > dist[0][0]:
                    heapq.heappop(dist)
                    heapq.heappush(dist, [d,x,y])
        
        
        res = []
        for i in range(k):
            d,x,y = heapq.heappop(dist)
            res.append([x,y])
        return res