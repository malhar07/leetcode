# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(list1):
            head = list1
            prev = temp = None

            while list1:
                temp = list1.next
                list1.next = prev

                prev = list1
                list1 = temp
            return prev, head
        
        dummy_head = ListNode(0,head)
        l = r = temp = dummy_head

        for i in range(right):
            if i == left-1:
                l = temp
            temp = temp.next
        r = temp.next
        temp.next = None

        reversed_head, reversed_tail = reverse(l.next)
        l.next = reversed_head
        reversed_tail.next = r

        return dummy_head.next


