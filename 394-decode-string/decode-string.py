class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                word = ""
                num = ""
                while stack and stack[-1] != "[":
                    word+=stack.pop()[::-1]
                word = word[::-1]
                stack.pop()
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                num = int(num[::-1])
                word = word*num
                stack.append(word)
        res = ""
        for w in stack:
            res += w
        return res
