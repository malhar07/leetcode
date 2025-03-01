# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        while left.next and left.next.val<x:
            left = left.next
        temp = left
        while temp.next:
            if temp.next.val < x:
                curr = temp.next
                temp.next = temp.next.next
                curr.next = left.next
                left.next = curr
                left = left.next
            else:
                temp = temp.next
        return dummy.next
        