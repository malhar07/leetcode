class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # dict1 = defaultdict(int)
        # for i in arr:
        #     dict1[i] += 1
        # count = 0
        # for i in sorted(dict1.values()):
        #     if k >= i:
        #         count += 1
        #         k-=i
        # return len(dict1) - count

        dict1 = defaultdict(int)
        for i in arr:
            dict1[i] += 1
        minH = []
        for key, val in dict1.items():
            heapq.heappush(minH, [val, key])
        while len(minH)>0 and k >= minH[0][0]:
            k-=minH[0][0]
            heapq.heappop(minH)
        return len(minH)

