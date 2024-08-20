class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # res = []
        # for elem in nums:
        #     res.append(elem**2)
        # res.sort()
        # return res
        # indx = 0
        # res=[]
        # while nums[indx] < 0:
        #     indx+=1
        # left_indx = indx-1
        # for i in range(len(nums)):
        #     if abs(nums[indx]) < abs(nums[left_indx]):
        #         res.append(nums[indx]**2)
        #         indx+=1
        #     else:
        #         res.append(nums[left_indx]**2)
        #         left_indx-=1
        # return res



        res = [0]*len(nums)

        left = 0
        right = len(nums)-1
        write = right

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[write] = nums[left]**2
                left+=1
                write-=1
            else:
                res[write] = nums[right]**2
                right-=1
                write-=1
        return res
