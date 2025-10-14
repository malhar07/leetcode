# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse_list( node):
            prev = None
            curr = node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp                
            return prev

        if not head:
            return None

        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        l2 = reverse_list(second_half)
        l1 = head

        while l2:
            temp = l2.next
            l2.next = l1.next
            l1.next = l2
            l2 = temp
            l1 = l1.next.next
        return head




        