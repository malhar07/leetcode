class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = abs(heapq.heappop(stones))
            stone2 = abs(heapq.heappop(stones))

            new_stone = abs(stone1-stone2)

            if new_stone:
                heapq.heappush(stones, -1*new_stone)
        stones.append(0)
        return abs(stones[0])