# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
        # head = TreeNode(0)
        # curr = head
        # carry = 0
        # while l1 and l2:
            
        #     add = l1.val + l2.val + carry
        #     curr.next = ListNode(add%10, None)
        #     carry = add//10
        #     curr = curr.next
        #     print(curr.val)

        #     l1 = l1.next
        #     l2 = l2.next
        # while l1:
        #     add = l1.val+carry
        #     curr.next = ListNode(add%10)
        #     carry = add//10

        #     curr = curr.next

        #     l1 = l1.next
        # while l2:
        #     add = l2.val+carry
        #     curr.next = ListNode(add%10)
        #     carry = add//10

        #     curr = curr.next

        #     l2 = l2.next
        # if carry == 1:
        #     curr.next = ListNode(1)
        # return head.next
        