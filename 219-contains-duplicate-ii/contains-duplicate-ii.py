class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1 = {}
        # if k == 0:
        #     return False
        
        for i in range(len(nums)):
            if nums[i] in dict1:
                return True
            else:
                dict1[nums[i]] = 1
            if len(dict1)>k:
                del dict1[nums[i-k]]
        return False