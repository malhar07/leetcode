# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1 -> 2  ->  3 -> 4 -> 5 -> 6
        dummy = ListNode(0)
        dummy.next = head
        right = left = dummy

        for i in range(n):
            right = right.next
        
        while right.next:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next