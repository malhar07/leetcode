class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = {i:[] for i in range(1,n+1)}
        min_heap = []

        for n1, n2, time in times:
            network[n1].append([n2,time])
        
        heapq.heappush(min_heap, [0,k])
        visited = set()
        total_time = {}

        while min_heap:
            # print(node)
            time, node  = heapq.heappop(min_heap)
            print(node)
            
            if node in visited:
                continue
            total_time[node] = time
            visited.add(node)

            for nei, t in network[node]:
                if nei not in visited:
                    heapq.heappush(min_heap,[time+t, nei])
        res = -1
        for i in range(1, n+1):
            if i not in total_time:
                return -1
            res = max(res,total_time[i])
        return res
                
                