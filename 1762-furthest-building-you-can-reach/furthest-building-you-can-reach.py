class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        count = 0

        for i in range(len(heights)-1):
            if heights[i+1] <= heights[i]:
                count+=1
            else:
                diff = heights[i+1] - heights[i]
                if ladders>0:
                    heapq.heappush(heap, diff)
                    count+=1
                    ladders-=1
                else:
                    if len(heap)>0 and heap[0] < diff:
                        diff = heapq.heappop(heap)
                        print("diff", diff)
                        heapq.heappush(heap, heights[i+1] - heights[i])

                    if bricks>=diff:
                        bricks-=diff
                        count+=1
                    else:
                        break
        return count