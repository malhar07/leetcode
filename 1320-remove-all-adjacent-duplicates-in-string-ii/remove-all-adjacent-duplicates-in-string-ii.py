class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if not stack or stack[-1][0] != i:
                stack.append((i,1))
            else:
                stack.append((i, stack[-1][1]+1))
            if stack[-1][1] == k:
                for j in range(k):
                    stack.pop()
        res = ""
        for i in stack:
            res+=i[0]
        return res