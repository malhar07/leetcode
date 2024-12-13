class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums[0])
        ans = ""

        def helper(s):
            nonlocal ans
            if len(s) == length:
                if s not in nums:
                    return s[:]
                    # ans = s[:]
                return
            
            add_zero = helper(s+"0")
            if add_zero:
                return add_zero
            
            return helper(s+"1")
        helper("")
        return helper("")
