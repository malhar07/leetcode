# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = head
        stack = []
        length = 0
        while temp:
            length += 1
            stack.append(temp.val)
            temp = temp.next
        max1 = 0
        temp = head
        print(stack)
        for i in range(length//2):
            sum1 = temp.val + stack.pop()
            if sum1 > max1:
                max1 = sum1
            temp = temp.next
        return max1