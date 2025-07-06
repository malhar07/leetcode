class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = {i:[] for i in range(1,n+1)}
        min_heap = []

        for n1, n2, time in times:
            network[n1].append([n2,time])
        
        heapq.heappush(min_heap, [0,k])
        visited = set()

        res = -1

        while min_heap:
            time, node  = heapq.heappop(min_heap)
            
            if node in visited:
                continue
            res = max(res, time)
            visited.add(node)

            for nei, t in network[node]:
                if nei not in visited:
                    heapq.heappush(min_heap,[time+t, nei])
        return res if len(visited) == n else -1