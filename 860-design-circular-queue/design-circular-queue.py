class Node:
    def __init__(self,val = -1, nxt = None):
        self.val = val
        self.nxt = nxt
class MyCircularQueue:

    def __init__(self, k: int):
        self.start = Node()
        temp = self.start
        for i in range(k-1):
            temp.nxt = Node()
            temp = temp.nxt
        temp.nxt = self.start
        self.end = temp
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.end = self.end.nxt
        self.end.val = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.start.val = -1
        self.start = self.start.nxt
        return True
        

    def Front(self) -> int:
        return self.start.val
        

    def Rear(self) -> int:
        return self.end.val

    def isEmpty(self) -> bool:
        return self.start.val == -1

    def isFull(self) -> bool:
        return self.end.nxt == self.start and self.start.val != -1


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()