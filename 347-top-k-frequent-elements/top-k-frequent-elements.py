class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        dict1 = defaultdict(int)

        for i in nums:
            dict1[i] += 1
        for key,val in dict1.items():
            heap.append([-val,key])
        print(heap)
        heapq.heapify(heap)

        for i in range(k):
            print(i)
            pair = heapq.heappop(heap)
            res.append(pair[1])
        return res