class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_pal(s,left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
            return True
        
        left = 0
        right = len(s)-1

        while left<right:
            if s[left] != s[right]:
                return check_pal(s, left, right-1) or check_pal(s, left+1, right)
            left+=1
            right-=1
        return True