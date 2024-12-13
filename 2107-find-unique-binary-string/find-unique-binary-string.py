class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums[0])
        ans = ""

        def helper(s):
            nonlocal ans
            # prin,t(s)
            if len(s) == length:
                if s not in nums:
                    # print(s)
                    ans = s[:]
                return
                
            helper(s+"0")
            # s=s[:-1]
            helper(s+"1")
        helper("")
        return ans
