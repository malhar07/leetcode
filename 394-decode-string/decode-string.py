class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i == "]":
                temp = ""
                num = ""

                while stack and not stack[-1].isdigit():
                    temp += stack.pop()[::-1]
                temp = temp[::-1][1:]

                while stack and stack[-1].isdigit():
                    num+=stack.pop()
                num = num[::-1]

                temp = temp*int(num)

                stack.append(temp)
            else:
                stack.append(i)
        
        return "".join(stack)