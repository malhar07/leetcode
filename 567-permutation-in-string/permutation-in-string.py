class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0]*26
        n = len(s1)
        for i in s1:
            count[ord(i) - ord('a')]+=1
        
        for i in range(len(s1)-1):
            if i < len(s2):
                count[ord(s2[i]) - ord('a')]-=1
            else:
                return False
        
        for i in range(len(s1)-1,len(s2)):
            count[ord(s2[i]) - ord('a')] -= 1
            isPerm = True
            for c in count:
                if c!= 0:
                    isPerm = False
                    break
            if isPerm:
                return True
            count[ord(s2[i-n+1]) - ord('a')]+=1
        return False