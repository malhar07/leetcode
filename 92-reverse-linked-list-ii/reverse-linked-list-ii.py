# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        l, r, temp = dummy, dummy, dummy

        def reverse(list1):
            prev = None

            while list1:
                temp = list1.next
                list1.next = prev 
                prev = list1
                list1 = temp
            return prev

        for i in range(right):
            if i == left-1:
                l = temp
            temp = temp.next
        r = temp.next
        temp.next = None

        

        reversed_head = reverse(l.next)
        l.next.next = r
        l.next = reversed_head
        return dummy.next