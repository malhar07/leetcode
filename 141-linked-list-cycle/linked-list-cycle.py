# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if not head or not head.next:
            return False
        fast = head.next

        while fast and fast.next:
            if fast.next == slow or fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False