# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        res = [None]*k

        temp = head
        if not head:
            return res

        while temp:
            length+=1
            temp = temp.next

        cnt = length//k
        extra = length%k

        temp = head
        end = -1
        
        for i in range(k):
            if not temp:
                return res
            start = temp
            for j in range(cnt):
                # if not temp:
                #     return res
                end = temp
                temp = temp.next

            if extra:
                # if not temp:
                #     return res
                end = temp
                temp = temp.next
                extra-=1

            end.next = None
            res[i] = start
        return res
            

            