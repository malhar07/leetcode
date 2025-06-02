class StockSpanner:

    def __init__(self):
        self.stack = []
        self.ind = 0
        

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price,self.ind))
            self.ind+=1
            return 1
        else:
            if self.stack[-1][0] > price:
                self.stack.append((price,self.ind))
                self.ind += 1
                return 1
            else:
                while self.stack and price>= self.stack[-1][0]:
                    self.stack.pop()
                if not self.stack:
                    res = self.ind+1
                else:
                    res = self.ind - self.stack[-1][1]
                self.stack.append((price,self.ind))
                self.ind+=1

                return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
[100,80,60,70,60,75]
[1,1,1,2,1]