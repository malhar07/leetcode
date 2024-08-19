# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # dict1={}
        # while headA:
        #     dict1[headA] = 1
        #     headA = headA.next
        # while headB:
        #     if headB in dict1:
        #         return headB
        #     headB = headB.next
        # return None

        node_dict = {}
        temp = headA
        node = None
        while temp:
            node_dict[temp] = 1
            temp = temp.next
        temp = headB
        while temp:
            if temp in node_dict:
                node = temp
                break
            temp = temp.next
        return node
        