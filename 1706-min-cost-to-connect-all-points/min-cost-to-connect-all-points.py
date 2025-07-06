class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_heap = [] # [weight, x, y]
        heapq.heappush(min_heap, [0,points[0][0], points[0][1]])

        visited = set()
        total_cost = 0

        while len(visited) < len(points):

            weight, x, y = heapq.heappop(min_heap)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            total_cost += weight
            if len(visited) == len(points):
                return total_cost
            for x1, y1 in points:
                if (x1,y1) not in visited:
                    new_weight = abs(x-x1) + abs(y-y1)
                    heapq.heappush(min_heap, [new_weight, x1, y1])
            
