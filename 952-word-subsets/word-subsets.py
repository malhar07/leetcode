class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        w2 = []
        bword = [0]*26
        for word in words2:
            arr = [0]*26
            for char in word:
                arr[ord(char)-97] += 1
                if arr[ord(char)-97] > bword[ord(char)-97]:
                    bword[ord(char)-97] = arr[ord(char)-97]
        print(bword)
        

        for word in words1:
            arr = [0]*26
            uni = True
            for char in word:
                arr[ord(char)-97] += 1
            for i in range(26):
                if arr[i] < bword[i]:
                    uni = False
                    break
            if uni:
                res.append(word)
        return res
        
        

