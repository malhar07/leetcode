# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        temp = head
        while l1 and l2:
            add = l1.val+l2.val+carry
            carry = add>9
            add = add%10

            new_node = ListNode(add)
            temp.next = new_node
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        if not l1:
            l1 = l2
        while l1:
            add = l1.val+carry
            carry = add>9
            add = add%10

            new_node = ListNode(add)
            temp.next = new_node
            temp = temp.next
            l1 = l1.next
        if carry:
            temp.next = ListNode(1)
        return head.next


