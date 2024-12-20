class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1={}
        if k == 0:
            return False

        for i in range(min(k, len(nums))):
            if nums[i] in dict1:
                return True
            dict1[nums[i]] = 1
        for i in range(k, len(nums)):
            if nums[i] in dict1:
                return True
            else:
                del dict1[nums[i-k]]
                dict1[nums[i]] = 1
        return False