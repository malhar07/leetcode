class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # curr_elem = nums[0]
        # count=0
        # for i in range(0,len(nums)):
        #     if count == 0:
        #         curr_elem = nums[i]
        #     if nums[i] == curr_elem:
        #         count+=1
        #     else:
        #         count-=1   
        # return curr_elem     

        count = 0
        curr = None
        for i in nums:
            if count == 0:
                curr = i
                count += 1
            else:
                if curr == i:
                    count += 1
                else:
                    count -= 1
        return curr