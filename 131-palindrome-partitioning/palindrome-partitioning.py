class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPal(s):
            left = 0
            right = len(s)-1

            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
            return True
        
        def helper(ind, pal):
            if ind == len(s):
                res.append(pal[:])
                return
            # if ind>= len(s):
            #     return

            for i in range(len(s[ind:])):
                if isPal(s[ind:ind+i+1]):
                    pal.append(s[ind:ind+i+1])
                    helper(ind+i+1, pal)
                    pal.pop()
        helper(0, [])
        return res