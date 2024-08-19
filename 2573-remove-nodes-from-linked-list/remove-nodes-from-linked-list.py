# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        ind = len(arr)-2
        max1 = arr[-1]
        while ind >= 0:
            temp = arr[ind]
            arr[ind] = max1
            if temp > max1:
                max1 = temp
            ind-=1
        temp = head
        ind = 1
        while temp.next:
            if temp.next.val < arr[ind]:
                temp.next = temp.next.next
                ind+=1
            else:
                temp = temp.next
                ind+=1
        print(arr)
        if head.val < arr[0]:
            return head.next
        
        return head