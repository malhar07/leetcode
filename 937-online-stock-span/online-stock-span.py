class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        if not self.stack:
            self.stack.append((price,1))
            return 1
        else:
            ind = len(self.stack)-1
            while ind >= 0 and self.stack[ind][0] <= price:
                res += self.stack[ind][1]
                ind -= self.stack[ind][1]
            self.stack.append((price, res))

        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)