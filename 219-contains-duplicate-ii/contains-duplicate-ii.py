class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_set = set()

        for ind in range(len(nums)):
            if len(num_set)>k:
                num_set.remove(nums[ind-k-1])

            if nums[ind] in num_set:
                return True
            num_set.add(nums[ind])
        return False