class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # def first(arr, target):
        #     left = 0
        #     right = len(arr)-1
        #     res = -1
        #     while left<=right:
        #         mid = left + (right-left)//2
        #         if arr[mid] == target:
        #             return mid
        #         elif arr[mid] > target:
        #             res =  mid
        #             right = mid-1
        #         else:
        #             left = mid+1
        #     if mid > 0 and ( abs(arr[mid-1]-target) <= abs(arr[mid] - target) ):
        #         mid-=1
        #     return mid
        # mid = first(arr, x)
        # left = mid
        # right = mid
        # for i in range(k-1):
        #     if left == 0:
        #         right+=1
        mid = len(arr)-1
        for ind, i in enumerate(arr):
            if i == x:
                mid = ind
                break
            if i > x:
                mid = ind
                if ind>0 and abs(x-arr[ind-1]) <= abs(x-arr[ind]):
                    mid = ind-1
                    break
        left = right = mid
        print(left)

        for i in range(k-1):
            if left == 0:
                right+=1
            elif right == len(arr)-1:
                left-=1
            elif abs(x - arr[left-1]) <= abs(x-arr[right+1]):
                left-=1
            else:
                right+=1
        return arr[left:right+1]

            