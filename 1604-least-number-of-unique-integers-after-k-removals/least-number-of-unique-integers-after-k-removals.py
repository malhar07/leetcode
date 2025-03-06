class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dict1 = defaultdict(int)
        heap = []
        for i in arr:
            dict1[i] += 1
        for i in dict1.values():
            heapq.heappush(heap, i)
        print(heap)
        while heap:
            if heap[0] <= k:
                k-=heap[0]
                heapq.heappop(heap)
            else:
                break
        return len(heap)
