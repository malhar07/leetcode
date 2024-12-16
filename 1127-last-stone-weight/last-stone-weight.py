class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones)>1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            heapq.heappush(stones, -abs(s1-s2))
        if len(stones)>0:
            return -stones[0]
        return 0
