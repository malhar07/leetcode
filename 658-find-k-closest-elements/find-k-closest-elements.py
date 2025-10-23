class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = len(arr)-1
        while idx>0 and arr[idx] > x:
            idx-=1
        if idx+1<len(arr) and abs(arr[idx+1] - x) < abs(arr[idx] - x):
            idx+=1
        left = right = idx
        while right-left+1 < k:
            if left-1 < 0 or (right+1 < len(arr) and abs(arr[left-1] - x) > abs(arr[right+1] - x)):
                right+=1
            else:
                left-=1
        return arr[left:right+1]