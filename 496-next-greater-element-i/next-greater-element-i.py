class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # stack = []
        # stack.append((nums2[0],0))
        # output = []
        # nge = [None]*len(nums2)
        # for i in range(1,len(nums2)):
        #     if nums2[i]<stack[-1][0]:
        #         stack.append((nums2[i],i))
        #     else:
        #         while stack and nums2[i] > stack[-1][0]:
        #             curr = stack.pop()
        #             nge[curr[1]] = nums2[i]
        #         stack.append((nums2[i],i))
        # while stack:
        #     curr = stack.pop()
        #     nge[curr[1]] = -1
        # print(nge)
        # for i in nums1:
        #     ind = nums2.index(i)
        #     output.append(nge[ind])
        # return output
        greater = [-1]*len(nums2)
  
        def helper(nums):
            stack = []
            for i in range(len(nums)):
                if not stack:
                    stack.append((nums[i], i))
                else:
                    while stack and stack[-1][0] < nums[i]:
                        ele, ind = stack.pop()
                        greater[ind] = nums[i]
                    stack.append((nums[i], i))
            # while stack:
            #     ele, ind = stack.pop()
            #     greater[ind] = -1
            return greater

        helper(nums2)
        print(greater)
        index_map = {}
        for i in range(len(nums2)):
            index_map[nums2[i]] = i
        res = []
        for num in nums1:
            ind = index_map[num]
            res.append(greater[ind])
        return res
        

