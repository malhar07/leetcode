# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        res = ListNode()
        ans = res
        temp = head

        while temp:
            if temp.val < x:
                ans.next = ListNode(temp.val)
                ans = ans.next
            temp = temp.next
        temp = head
        while temp:
            if temp.val >= x:
                ans.next = ListNode(temp.val)
                ans = ans.next
            temp = temp.next
        return res.next