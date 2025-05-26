class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def search(arr, target):
            left = 0
            right = len(arr)-1
            # found = False
            res = -1
            while left<=right:
                mid = left + (right-left)//2
                if arr[mid] == target:
                    # found = True
                    res = mid
                    left = mid+1
                    # return mid
                if arr[mid] <= target:
                    left = mid+1
                else:
                    right = mid-1
            return res
        
        for ind, num in enumerate(numbers):
            if ind==0 or numbers[ind] != numbers[ind-1]:
                mid = search(numbers, target-num)
                if  mid != -1:
                    return[ind+1, mid+1]