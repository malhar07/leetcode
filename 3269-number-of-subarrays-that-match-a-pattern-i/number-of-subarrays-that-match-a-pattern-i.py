class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        res = 0
        for i in range(len(nums) - len(pattern)):
            found = True
            for j in range(len(pattern)):
                if pattern[j] == 1 and nums[i+j] >= nums[i+j+1]:
                    found = False
                    break
                elif pattern[j] == 0 and nums[i+j] != nums[i+j+1]:
                    found = False
                    break
                elif pattern[j] == -1 and nums[i+j] <= nums[i+j+1]:
                    found = False
                    break

            if found:
                print(i)
                res+=1
                
        return res
             