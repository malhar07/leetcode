# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        leftA = list1
        right = list2
        for i in range(a-1):
            leftA = leftA.next
        while right.next:
            right = right.next
        rightA = leftA
        for i in range(b-a+1):
            rightA = rightA.next
        leftA.next = list2
        right.next = rightA.next
        return list1