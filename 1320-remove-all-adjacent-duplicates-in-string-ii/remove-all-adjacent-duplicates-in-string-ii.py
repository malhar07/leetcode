class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if not stack or stack[-1][0] != i:
                stack.append((i,1))
            else:
                stack[-1] = (i,stack[-1][1]+1)
                # for j in range(k-1):
                #     stack.pop()
                # stack.append((i, stack[-1][1]+1))
            if stack[-1][1] == k:
                # for j in range(k):
                    stack.pop()
        res = ""
        for i in stack:
            res+=i[0]*i[1]
        return res