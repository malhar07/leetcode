# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = TreeNode(0)
        curr = head
        carry = 0
        while l1 and l2:
            
            add = l1.val + l2.val + carry
            curr.next = ListNode(add%10, None)
            carry = add//10
            curr = curr.next
            print(curr.val)

            l1 = l1.next
            l2 = l2.next
        while l1:
            add = l1.val+carry
            curr.next = ListNode(add%10)
            carry = add//10

            curr = curr.next

            l1 = l1.next
        while l2:
            add = l2.val+carry
            curr.next = ListNode(add%10)
            carry = add//10

            curr = curr.next

            l2 = l2.next
        if carry == 1:
            curr.next = ListNode(1)
        return head.next
        