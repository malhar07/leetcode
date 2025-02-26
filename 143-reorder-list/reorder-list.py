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
        # def reverse(head):
        prev = None
        curr = fast
        # curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # return prev
        # def merge(l1, l2):
        #     head = l1
        l2 = prev
        l1 = head
        while l2:
            curr = l2
            l2 = l2.next
            curr.next = l1.next
            l1.next = curr

            l1 = l1.next.next
        return head
            # return head
        # l2 = reverse(fast)
        # print(l2)
        # return merge(head, l2)
