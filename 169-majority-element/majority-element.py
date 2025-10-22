class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_majority_ele = nums[0]
        curr_count = 1

        for num in nums[1:]:
            if curr_count == 0:
                curr_count+=1
                curr_majority_ele = num
            else:

                if num == curr_majority_ele:
                    curr_count += 1
                else:
                    curr_count -= 1
        return curr_majority_ele