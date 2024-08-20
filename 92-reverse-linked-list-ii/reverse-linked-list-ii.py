# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # temp = head
        # curr = None
        # end = None
        # while temp.next:
        #     if temp.next.val == left:
        #         prev = temp
        #         curr = temp.next
        #     if temp.next.val == right:
        #         end = temp.next
        #     temp = temp.next
        # if end == None or curr == None:
        #     return head
        # while True:
        #     temp = curr.next
        #     curr.next = end.next
        #     end.next = curr
        #     prev.next = temp
        #     curr = prev.next
        #     if curr == end:
        #         break
        # return head

        if left == right:
            return head

        root = ListNode(0,head)


        start, end = root, root

        for i in range(right):
            end = end.next
            if i < left-1:
                start = start.next
        print(start.val, "->", end.val)
        # root = ListNode(0, None)
        prev = end.next
        curr=start.next
        temp = curr

        start.next = end
        ind=0


        for i in range(right-left+1):
            ind+=1
            print(ind)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return root.next

