class StockSpanner:

    def __init__(self):
        self.stack = []
        self.ind = 0

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append([price,1])
            self.ind+=1
            return 1
        else:
            res = 1
            i = self.ind - 1

            while i >= 0 and self.stack[i][0] <= price:
                res += self.stack[i][1]
                i-= self.stack[i][1]
            self.stack.append([price, res])
            self.ind += 1
            return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)