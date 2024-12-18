# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        temp = head

        res = [None]*k

        if not head:
            return res

        while temp:
            length+=1
            temp = temp.next

        cnt = length//k
        extra = length%k

        temp = head
        prev = -1
        
        for i in range(k):
            dummy = temp
            for j in range(cnt):
                if not temp:
                    return res
                prev = temp
                temp = temp.next

            if extra:
                if not temp:
                    return res
                prev = temp
                temp = temp.next
                extra-=1
            prev.next = None
            res[i] = dummy
        return res
            

            