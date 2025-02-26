# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # stack = []
        # temp = head
        # length = 0
        # while temp:
        #     stack.append(temp)
        #     temp = temp.next
        #     length+=1
        # temp = head
        # for i in range(length//2):
        #     curr = stack.pop()
        #     curr.next = temp.next
        #     temp.next = curr
        #     temp = temp.next.next
        # temp.next = None
        # return head
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        prev = None
        # curr = fast

        while fast:
            temp = fast.next
            fast.next = prev
            prev = fast
            fast = temp

        # l2 = prev
        l1 = head
        while prev:
            curr = prev
            prev = prev.next
            curr.next = l1.next
            l1.next = curr

            l1 = l1.next.next
        return head
