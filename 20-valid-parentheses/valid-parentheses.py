class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = "[{("
        closing_bracket = {
            "{":"}",
            "[":"]",
            "(":")"
        }


        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
            else:
                if stack and ((bracket == ")" and stack[-1] == "(") or (bracket == "}" and stack[-1] == "{") or (bracket == "]" and stack[-1] == "[")):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0