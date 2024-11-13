class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for ind, i in enumerate(nums):
            # if i > 0:
            #     return []
            left = ind+1
            right = len(nums)-1

            while left < right:
                if i + nums[left] + nums[right] == 0:
                    res.add((i, nums[left], nums[right]))
                    left+=1
                    right-=1
                elif i + nums[left] + nums[right] > 0:
                    right-=1
                else:
                    left+=1
                # while left < len(nums) and nums[left] == nums[left-1]:
                #     left+=1
                # while right > 0 and right != len(nums)-1 and nums[right] == nums[right+1]:
                #     right-=1
        return [[x[0], x[1], x[2]] for x in res]
        # return [[0,0,0]]
        
        for x in res:
            print(x[0])
        return [[]]

            