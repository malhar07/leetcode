class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dict1 = {0:-1}
        presum = 0
        for ind, i in enumerate(nums):
            presum += i
            rem = presum%k

            if rem in dict1:
                if ind-dict1[rem]>1:
                    return True
            else:
                dict1[rem] = ind
        return False

        #     if ind>0 and presum%k == 0:
        #         return True
        #     temp = presum
        #     while temp>=0:
        #         # print(temp)
        #         if temp in dict1 and ind-dict1[temp]!=1:
        #             return True
        #         else:
        #             temp-=k
        #     if presum not in dict1:
        #         dict1[presum] = ind
        # return False