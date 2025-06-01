class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-1
        res = -1

        while left<=right:
            mid = left + (right-left)//2

            if arr[mid] < x:
                res = mid
                left = mid+1
            elif arr[mid] == x:
                res = mid
                right = mid-1
            else:
                right = mid-1
        res = max(res,0)
        mid = res
        if mid+1<len(arr):
            if abs(arr[mid] - x) > abs(arr[mid+1]-x):
                mid = mid+1
        
        left = right = mid
        for i in range(k-1):
            if left == 0:
                right+=1
            elif right == len(arr)-1:
                left-=1
            else:
                if abs(arr[left-1]-x) <= abs(arr[right+1]-x):
                    left-=1
                else:
                    right+=1
        return arr[left:right+1]
