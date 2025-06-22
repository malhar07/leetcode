# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(101)
        dummy.next = head
        temp = head
        prev = dummy

        # curr = None
        while temp:
            curr = temp.val
            del_node = False
            while temp.next and temp.next.val == curr:
                del_node = True
                temp.next = temp.next.next
            if del_node:
                prev.next = temp.next
                temp = prev
            prev = temp
            temp = temp.next
        return dummy.next