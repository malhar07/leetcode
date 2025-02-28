class Node:
    def __init__(self,val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        new_node = Node(homepage)
        self.curr = new_node

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.curr.next = new_node
        new_node.prev = self.curr
        self.curr = new_node

    def back(self, steps: int) -> str:
        count = 0
        while self.curr.prev:
            count += 1
            self.curr = self.curr.prev
            if count == steps:
                return self.curr.val
        return self.curr.val

    def forward(self, steps: int) -> str:
        count = 0
        while self.curr.next:
            count += 1
            self.curr = self.curr.next
            if count == steps:
                return self.curr.val
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)