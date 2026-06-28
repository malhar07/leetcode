class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-1

        while (right-left+1) > k:
            if abs(x-arr[left]) <= abs(x-arr[right]):
                right-=1
            else:
                left +=1
        return arr[left:right+1]


# [1,1,2,3,4,5,6,7,]