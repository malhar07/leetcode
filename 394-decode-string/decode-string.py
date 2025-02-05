class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                temp = ""
                while stack[-1] != '[':
                    temp += stack.pop()[::-1]
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num+=stack.pop()
                
                stack.append(temp[::-1] * int(num[::-1]))
        return "".join(stack)
# zzz2[yypq4[jkjkef]]