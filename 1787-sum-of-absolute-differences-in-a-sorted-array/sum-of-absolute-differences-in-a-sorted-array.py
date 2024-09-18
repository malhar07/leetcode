class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre1 = [0]*len(nums)
        pre2 = [0]*len(nums)

        pre1[-1] = nums[-1]
        pre2[0] = nums[0]
        ind = len(nums)-2
        while ind >=0:
            pre1[ind] = nums[ind] + pre1[ind+1]
            pre2[len(nums)-1 - ind] = nums[len(nums)-1 - ind] + pre2[len(nums)-1 - ind - 1]
            ind-=1

        res = []
        for ind, i in enumerate(pre1):
            res.append(i - (len(nums)-ind)*nums[ind])
            res[ind] += (ind+1)*nums[ind] - pre2[ind]

        return res