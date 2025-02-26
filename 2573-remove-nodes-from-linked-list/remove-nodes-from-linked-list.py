# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 13,10,7,5,4,2,8
        
        20,5,2,13,3,8
        # start = ListNode()
        # start.next = head
        # ptr = start
        # temp = start
        # _min = 100001

        # while ptr.next:
        #     _min = min(_min, ptr.next.val)
        #     print(_min)
        #     if ptr.next.val > _min:
        #         while temp.next.val> ptr.next.val:
        #             temp = temp.next
        #         temp.next = ptr.next
        #         ptr = temp.next
        #         temp = start
        #     else:
        #         ptr = ptr.next
        # return start.next
        arr = []
        temp = head
        if not head:
            return None
        while temp:
            arr.append([temp.val,False])
            temp = temp.next
        curr = arr[-1][0]
        for i in range(len(arr)-1,-1,-1):
            if arr[i][0] < curr:
                arr[i][1] = True
            else:
                curr = arr[i][0]
        print(arr)
        start = ListNode()
        temp = start
        start.next = head
        ind = 0
        while temp.next:
            if arr[ind][1] == True:
                temp.next = temp.next.next
            else:
                temp = temp.next
            ind+=1
            
        return start.next