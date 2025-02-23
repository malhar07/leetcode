# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def ispal(s):
            left = 0
            right = len(s)-1

            while left < right:
                if s[left] != s[right]:
                    return False
                left +=1
                right-=1
            return True
        
        s = ""
        while head:
            s+=str(head.val)
            head = head.next
        return ispal(s)