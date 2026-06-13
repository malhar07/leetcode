class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "]":
                string1 = ""
                num = ""
                # Get full char string
                while stack and stack[-1].isalpha():
                    string1 += stack.pop()
                string1 = string1[::-1]

                #Pop out "["
                stack.pop()

                #Get full number
                while stack and stack[-1].isnumeric():
                    num += stack.pop()
                num = int(num[::-1])
                string2 = string1*num

                #Append reverse string
                stack.append(string2[::-1])

            else:
                stack.append(char)
        # print(stack)
        res = ""
        for s in stack:
            res += s[::-1]
        return res