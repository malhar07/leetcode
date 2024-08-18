# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # deq = deque()
        # temp = head
        # while temp:
        #     deq.append(temp.val)
        #     temp = temp.next
        
        # while deq:
        #     if len(deq) >1:
        #         if deq.popleft() != deq.pop():
        #             return False
        #     else:
        #         break
        # return True
        # temp = head
        # count = 0
        # while temp:
        #     count+=1
        #     temp = temp.next
        # count+=1
        # temp = head
        # for i in range(int(count/2)):
        #     temp = temp.next
        # curr = temp
        # prev = None
        # while curr:
        #     t = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = t
        # temp = prev
        # while temp:
        #     if temp.val != head.val:
        #         return False
        #     temp = temp.next
        #     head = head.next
        # return True
        pal = ""
        temp = head
        while temp:
            pal+=str(temp.val)
            temp = temp.next
        return pal == pal[::-1]