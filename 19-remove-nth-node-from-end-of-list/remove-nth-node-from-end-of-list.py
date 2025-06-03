# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        for i in range(n):
            temp=temp.next
        # dummy = ListNode()
        if not temp:
            return head.next
        left = head
        while temp.next:
            temp=temp.next
            left = left.next
        left.next = left.next.next
        return head
        