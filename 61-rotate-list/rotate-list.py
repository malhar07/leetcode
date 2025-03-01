# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        temp = head
        if not head:
            return None
        while temp:
            length += 1
            temp = temp.next
        k%=length
        temp = head
        for i in range(k):
            temp = temp.next
        left = head
        while temp.next:
            temp = temp.next
            left = left.next
        temp.next = head
        new_head = left.next
        left.next = None
        return new_head