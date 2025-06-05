class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        self.left_count = 0
    def addNum(self, num: int) -> None:
        if not self.left or num<= -self.left[0]:
            heapq.heappush(self.left,-num)
            self.left_count+=1
        else:
            heapq.heappush(self.right, num)
            self.left_count-=1
        
        if self.left_count>=2:
            val = heapq.heappop(self.left)
            heapq.heappush(self.right,-val)
            self.left_count = 0
        elif self.left_count <= -2:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left,-val)
            self.left_count = 0



    def findMedian(self) -> float:
        if self.left_count == 1:
            return -self.left[0]
        elif self.left_count == -1:
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()