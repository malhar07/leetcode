class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                word = ""
                num = ""
                while stack and stack[-1]!="[":
                    word+=stack.pop()
                stack.pop()
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                num = num[::-1]
                stack.append(int(num)*word)
        for word in stack:
            res+=word[::-1]
        return res