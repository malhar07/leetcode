class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # nums.sort()
        # count = 0
        # curr = 0
        # res = 0

        # for i in range(len(nums)):
        #     if curr != nums[i]:
        #         res += (count*(count-1)) // 2
        #         curr = nums[i]
        #         count = 1
        #     else:
        #         count+=1
        # return res+(count*(count-1)) // 2
        dict1 = {}
        count = 0
        for i in nums:
            # if i in dict1:
                # count+= dict1[i]
            dict1[i] = dict1.get(i, 0)+1
        for v in dict1.values():
            count += (v*(v-1))//2
        return count