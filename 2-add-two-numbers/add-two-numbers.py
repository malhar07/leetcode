# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        head = dummy

        while l1 and l2:
            _add = l1.val+l2.val+carry
            carry = _add//10
            _add = _add%10

            head.next = ListNode(_add)
            head=head.next
            l1 = l1.next
            l2=l2.next
    
        if l1:
            while l1:
                _add = l1.val+carry
                carry = _add//10
                _add = _add%10

                head.next = ListNode(_add)
                head=head.next
                l1 = l1.next

        if l2:
            while l2:
                _add = l2.val+carry
                carry = _add//10
                _add = _add%10
                
                head.next = ListNode(_add)
                head=head.next
                l2 = l2.next
        if carry > 0:
            head.next = ListNode(1)
        return dummy.next
        