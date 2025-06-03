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

        def reverse(head):
            if not head:
                return None
            
            prev = temp = None

            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev


        if not head:
            return None
        slow = head
        fast = slow.next
        #1) partition list in half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        
        #2)reverse the second half
        list2 = reverse(fast)

        #3) Merge Alternately
        list1 = head

        while list1 and list2:
            temp = list2.next

            list2.next = list1.next
            list1.next = list2

            list2 = temp
            list1 = list1.next.next
        return head



        