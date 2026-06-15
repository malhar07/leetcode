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
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        #Reverse the second half
        prev = None
        temp = curr = head2

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev

        res = head
        temp = head
        temp2 = head2
        while head2:
            head2 = temp2.next
            temp2.next = temp.next
            temp.next = temp2

            temp = temp.next.next
            temp2 = head2
        return res