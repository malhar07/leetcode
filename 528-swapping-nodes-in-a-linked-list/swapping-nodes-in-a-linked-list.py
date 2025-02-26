# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = head
        right = head
        for i in range(k-1):
            left = left.next
        temp = left
        right = head

        while temp.next:
            temp=temp.next
            right = right.next
        left.val, right.val = right.val, left.val
        return head