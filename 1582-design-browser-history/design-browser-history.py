class BrowserHistory:
    # e,h,w    k,c,i,u
    # e,k,i,e,w

    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.left = 0
        self.right = 0
        self.curr = 0

    def visit(self, url: str) -> None:
        if self.curr < self.right:
            self.arr[self.curr+1] = url
            self.right = self.curr+1
            self.curr+=1
            self.arr = self.arr[self.left:self.right+1]
        elif self.curr == self.right:
            self.arr.append(url)
            self.right += 1
            self.curr = self.right

    def back(self, steps: int) -> str:
        if self.curr-steps >= 0:
            val =  self.arr[self.curr-steps]
            self.curr -= steps
        else:
            self.curr = 0
            return self.arr[0]
        return val

        

    def forward(self, steps: int) -> str:
        if self.curr + steps <= self.right:
            val = self.arr[self.curr+steps]
            self.curr += steps
        else:
            self.curr = self.right
            return self.arr[self.right]
        return val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)