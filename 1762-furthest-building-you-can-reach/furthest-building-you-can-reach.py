class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        total_height = 0
        ladder_height = 0
        minH = []
        # res = 0
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            else:
                heapq.heappush(minH, diff)
                ladder_height += diff
                # ladders-=1

                if len(minH) > ladders:
                    ladder_height -= heapq.heappop(minH)
                    # ladders+=1

                total_height += diff

                if bricks < total_height-ladder_height:
                    return i
        return len(heights)-1
                
                
                    

        
