class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = k-1

        for i in range(len(arr)-k):
            if abs(arr[left] - x) <= abs(arr[right+1] - x):
                if arr[left] == arr[right+1]:
                    left+=1
                    right+=1
                else:
                    break
            # elif abs(arr[left] - x) == abs(arr[right+1] - x):

            else:
                left+=1
                right+=1
        return arr[left:right+1]