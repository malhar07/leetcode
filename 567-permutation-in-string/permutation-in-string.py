class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = [0]*26
        count2 = [0]*26
        count = 0

        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')] += 1
            count2[ord(s2[i])-ord('a')] += 1
        for i in range(26):
            if count1[i] == count2[i]:
                count+=1
        
        for i in range(len(s1), len(s2)):
            if count == 26:
                return True
            if count2[ord(s2[i-len(s1)]) - ord('a')] == count1[ord(s2[i-len(s1)]) - ord('a')]:
                count-=1
            count2[ord(s2[i-len(s1)]) - ord('a')]-=1
            if count2[ord(s2[i-len(s1)]) - ord('a')] == count1[ord(s2[i-len(s1)]) - ord('a')]:
                count+=1


            if count2[ord(s2[i])-ord('a')] == count1[ord(s2[i])-ord('a')]:
                count-=1
            count2[ord(s2[i])-ord('a')] += 1
            if count2[ord(s2[i])-ord('a')] == count1[ord(s2[i])-ord('a')]:
                count+=1
        return count == 26

        