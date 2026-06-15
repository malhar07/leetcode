class Node:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.count = 0
        self.capacity = capacity
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    
    def add(self, key, val):

        node = Node(key, val)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

        return node
    
    def remove_from_head(self):

        temp = self.head.next
        self.head.next = temp.next
        temp.next.prev = self.head
        temp.next = None
        temp.prev = None

        return temp
    
    def remove(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = None
        node.prev = None
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]

            self.remove(node)

            new_node = self.add(node.key, node.val)
            self.cache[key] = new_node

            return self.cache[key].val



    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        else:
            self.count += 1

        new_node = self.add(key,value)
        self.cache[key] = new_node
        

        if self.count > self.capacity:
            temp = self.remove_from_head()
            del self.cache[temp.key]
            self.count -= 1

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)