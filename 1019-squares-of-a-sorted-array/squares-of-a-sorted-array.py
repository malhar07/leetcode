class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        left = 0
        right = len(res)-1
        write = len(res)-1

        while left<=right:
            if abs(nums[left]) > abs(nums[right]):
                maxx = nums[left]
                left+=1
            else:
                maxx=nums[right]
                right-=1
            res[write] = maxx**2
            write-=1
        return res