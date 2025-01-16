class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        arr = [0]*26
        res = []
        if len(p)>len(s):
            return []

        for i in range(len(p)):
            arr[ord(p[i])-97] += 1
        for i in range(len(p)-1):
            arr[ord(s[i]) - 97] -= 1
        
        
        for i in range(len(p)-1, len(s)):
            arr[ord(s[i]) - 97] -= 1

            isana = True
            for count in arr:
                if count != 0:
                    isana = False
                    break
            
            if isana:
                res.append(i - len(p)+1)
            
            arr[ord(s[i-len(p)+1]) - 97] += 1
            
            
        return res
            