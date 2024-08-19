# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         temp = head
#         stack = []
#         if head is None:
#             return None
#         while temp.next is not None:
#             stack.append(temp)
#             temp=temp.next
        
#         root = temp
#         temp = root
#         while stack:
#             temp.next = stack.pop()
#             temp = temp.next
#         temp.next = None
#         return root

        # curr = head
        # prev = None
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # return prev

        prev = None
        curr = head
        temp = head
        ind=0

        while curr:
            ind+=2
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            print(ind)
        return prev

        