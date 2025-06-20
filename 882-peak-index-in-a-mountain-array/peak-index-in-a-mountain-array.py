class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) -1 

        while left<=right:
            mid = left + (right-left)//2

            if mid == 0 or arr[mid] > arr[mid-1]:
                if mid == len(arr)-1 or arr[mid+1]< arr[mid]:
                    return mid
                else:
                    left = mid+1
            else:
                right = mid-1
        

