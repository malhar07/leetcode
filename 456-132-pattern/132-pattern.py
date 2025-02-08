class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [(nums[0], nums[0])]
        minn = nums[0]
        for i in nums[1:]:
            while stack and i >= stack[-1][0]:
                stack.pop()
            if stack and i > stack[-1][1]:
                return True
            # if not stack or i <= stack[-1][0]:
            #     stack.append((i,minn))
            # else:
                
            #         return True
            stack.append((i,minn))
            minn = min(minn,i)
        return False