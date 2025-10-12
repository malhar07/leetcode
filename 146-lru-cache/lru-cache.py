class node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {}
        self.head = node(0,0)
        self.tail = node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

        

    def get(self, key: int) -> int:
        if key in self.lru:
            v = self.lru[key].val
            self.remove(key)
            self.add(key, v)
            return v
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru[key].val = value
            self.remove(key)
            self.add(key,value)
        else:
            if len(self.lru) >= self.capacity:
                least = self.tail.prev.key
                self.remove(least)
                del self.lru[least]
            #new_node = node(key, value)
            new_node = self.add(key, value)
            self.lru[key] = new_node
        

    
    def add(self, k, v):
        nn = node(k,v)
        nn.next = self.head.next
        nn.prev = self.head
        self.head.next = nn
        nn.next.prev = nn

        self.lru[k] = nn

        return nn

    def remove(self, key):
        nn = self.lru[key]
        nn.next.prev = nn.prev
        nn.prev.next = nn.next



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)