# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        index = dummy
        while l1 or l2 or carry:
            num1 = num2 = 0
            if l1:
                num1 = l1.val
            if l2:
                num2 = l2.val
            add = num1 + num2 + carry
            index.next = ListNode(add%10)
            carry = add//10
            index = index.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next





