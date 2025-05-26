class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        e1, count1, e2, count2 = None, 0, None, 0
        res = []

        for num in nums:
            if num == e1:
                count1 += 1
            elif e2 == num:
                count2 += 1
            elif count1 == 0:
                e1 = num
                count1 = 1
            elif count2 == 0:
                e2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        # return [e1, e2]
        count1, count2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == e1:
                count1+=1
            if nums[i] == e2:
                count2+=1
        if count1> len(nums)//3:
            res.append(e1)
        if count2>len(nums)//3:
            res.append(e2)
        return res
    