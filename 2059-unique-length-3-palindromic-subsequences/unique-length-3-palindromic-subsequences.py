class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        seen = defaultdict(int)
        temp = {}
        count = 0

        start = 0
        end = len(s)-1

        while start < len(s)-2:
            temp = {}
            if s[start] not in seen:
                while s[end] != s[start]:
                    end-=1
                end-=1
                while end>start:
                    if s[end] not in temp:
                        temp[s[end]] = 1
                        count+=1
                    end-=1
            seen[s[start]] +=1
            start +=1
            end = len(s)-1
        print(seen)
        return count
            