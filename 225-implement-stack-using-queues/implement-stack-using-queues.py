import queue
class MyStack:

    def __init__(self):
        self.q = queue.Queue()
        # self.top = None

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        temp = queue.Queue()
        while self.q.qsize()>1:
            temp.put(self.q.get())

        top = self.q.get()
        self.q = temp
        return top


    def top(self) -> int:
        temp = queue.Queue()
        while self.q.qsize()>1:
            temp.put(self.q.get())

        top = self.q.get()
        temp.put(top)
        self.q = temp
        return top
        

    def empty(self) -> bool:
        return self.q.qsize() == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()