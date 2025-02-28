class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        ind = 0
        temp = self.head
        print(self.length)
        while temp:
            print(ind, " ", temp.val)
            if ind == index:
                return temp.val
            ind+=1
            temp = temp.next
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

            

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.length:
            return
        if index == 0:
            self.addAtHead(val)
            return
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        new_node = Node(val)
        new_node.next = temp.next
        temp.next = new_node
        if new_node.next is None:
            self.tail = new_node
        self.length +=1

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.length or index<0:
            return 
        temp = self.head
        if index == 0:
            self.head=self.head.next
            if self.length == 1:
                self.tail = None
        else:
            
            for i in range(index-1):
                temp = temp.next
            temp.next = temp.next.next
        if temp.next is None:
            self.tail = temp
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
