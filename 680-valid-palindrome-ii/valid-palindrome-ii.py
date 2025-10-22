class Solution:
    def validPalindrome(self, s: str) -> bool:
        self.del_char = False

        def check_pal(strng):
            left = 0
            right = len(strng)-1

            while left < right:
                if strng[left]!=strng[right]:
                    if self.del_char == False:
                        self.del_char = True
                        return check_pal(strng[left:right]) or check_pal(strng[left+1:right+1])
                    else:
                        return False
                left +=1
                right -= 1
            return True
        return check_pal(s)

                    