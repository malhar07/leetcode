class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.Next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict1 = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head



    def get(self, key: int) -> int:
        if key in self.dict1:
            node = self.dict1[key]
            self.remove(self.dict1[key])
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict1:
            self.remove(self.dict1[key])
        elif len(self.dict1) >= self.capacity:
            k = self.tail.prev.key
            del self.dict1[k]
            self.remove(self.tail.prev)
        node = Node(key, value)
        self.add(node)
        self.dict1[key] = node
    
    def add(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
    
    def remove(self,node):
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)