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
        stack = []

        temp = head
        
        while temp:

            stack.append(temp)
            temp = temp.next
        # print(stack)
        
        root = ListNode(0, None)
        temp = root
        left = head
        right = stack.pop()
        ind = 0
        while left != right and left.next != right:
            temp.next = left
            temp = temp.next
            left = left.next

            temp.next = right
            temp = temp.next
            ind+=1
            print(ind)
            # print(left, " ->÷", right)

            
            right = stack.pop()

        temp.next = left
        temp = temp.next
        if left == right:
            temp.next = None
        else:
            temp.next = right
            temp.next.next = None
        return root.next