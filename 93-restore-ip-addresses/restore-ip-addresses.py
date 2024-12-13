class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) < 4:
            return []
        def isValid(num):
            if len(num)== 1:
                return True
            if int(num) < 256 and len(num) == len(str(int(num))):
                return True
            return False
        def helper():
            for i in range(1,len(s)-2):
                for j in range(i+1,len(s)-1):
                    for k in range(j+1,len(s)):
                        if isValid(s[:i]) and isValid(s[i:j]) and isValid(s[j:k]) and isValid(s[k:]):
                            res.append(s[:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:])

        helper()
        return res
