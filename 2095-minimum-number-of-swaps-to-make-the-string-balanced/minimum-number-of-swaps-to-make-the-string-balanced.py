class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        count = 0

        for i in s:
            if i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    count += 1
                else:
                    stack.pop()
        print(count)
        return (count+1)//2