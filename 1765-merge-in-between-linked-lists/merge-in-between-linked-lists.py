# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # temp = list1
        left = list1
        right = list1
        for i in range(b-1):
            right = right.next
        for i in range(a-1):
            left = left.next
        end = list2
        while end.next:
            end = end.next
        end.next = right.next.next
        left.next = list2
        return list1
