class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # for i in s:
        #     if i in "({[":
        #         stack.append(i)
        #     else:
        #         if len(stack)>0:
        #             if i == ")" and stack.pop() != "(":
        #                 return False
        #             if i == "]" and stack.pop() != "[":
        #                 return False
        #             if i == "}" and stack.pop() != "{":
        #                 return False
        #         else:
        #             return False
        # # return True
        # if len(stack) == 0:
        #     return True
        # else:
        #     return False
                
        stack = []
        brack = ""

        for i in s:
            if i in ['(', '{', "["]:
                stack.append(i)
            else:
                if stack:
                    brack = stack.pop()
                    if (brack == '(' and i == ')') or (brack == '{' and i == '}') or (brack == '[' and i == ']'):
                        continue
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0