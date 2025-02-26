# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None

        prev = None
        while fast:
            temp = fast.next
            fast.next = prev
            prev = fast
            fast = temp
        res = 0
        first,second = head, prev
        while second:
            res = max(res, first.val+second.val)
            first = first.next
            second = second.next
        return res
