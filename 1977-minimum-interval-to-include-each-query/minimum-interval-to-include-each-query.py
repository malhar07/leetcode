class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(reverse=True)
        squeries = sorted(enumerate(queries), key = lambda x : x[1]) #arr of [query, old_ind]
        res = [-1] * len(queries)

        active_inter = []# heap of (size, right end_point)

        for q in squeries:
            while active_inter and active_inter[0][1] < q[1]:
                heapq.heappop(active_inter)
            
            while intervals and intervals[-1][0] <= q[1]:
                s,e = intervals.pop()
                size = e-s+1
                if e >= q[1]:
                    heapq.heappush(active_inter, (size,e))
            if active_inter:
                res[q[0]] = active_inter[0][0]
        return res
                
