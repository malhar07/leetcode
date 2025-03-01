# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        temp = dummy
        

        while temp.next and temp.next.next:
            left = temp.next
            right = left.next


            left.next = right.next
            right.next = left
            temp.next = right

            # if dummy.val == -1:
            #     dummy = right
            #     dummy.val = 0
            temp = temp.next.next
        return dummy.next