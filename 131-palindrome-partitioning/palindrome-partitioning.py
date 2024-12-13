class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        dict1 = {}
        def isPal(s):
            left = 0
            right = len(s)-1

            while left < right:
                if s[left] != s[right]:
                    dict1[s] = False
                    return False
                left+=1
                right-=1
            dict1[s] = True
            return True
        
        def helper(ind, pal):
            if ind == len(s):
                res.append(pal[:])
                return

            for i in range(len(s[ind:])):
                curr = s[ind:ind+i+1]
                if curr in dict1:
                    if dict1[curr]:
                        pal.append(s[ind:ind+i+1])
                        helper(ind+i+1, pal)
                        pal.pop()
                else:
                    if isPal(curr):
                        pal.append(curr)
                        helper(ind+i+1, pal)
                        pal.pop()

                
                    
        helper(0, [])
        return res