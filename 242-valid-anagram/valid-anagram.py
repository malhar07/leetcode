class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = defaultdict(int)
        for char in s:
            char_dict[char] += 1
        for char in t:
            char_dict[char] -= 1
        
        for val in char_dict.values():
            if val != 0:
                return False
        return True
