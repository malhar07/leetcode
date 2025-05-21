class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = [0]*26

        for char in s:
            char_dict[ord(char)-ord('a')] +=1
        for char in t:
            char_dict[ord(char)-ord('a')] -=1
        print(char_dict)
        for char_count in char_dict:
            if char_count != 0:
                return False
        return True
         