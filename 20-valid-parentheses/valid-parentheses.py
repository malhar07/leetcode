class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        stack = []

        for b in s:
            if b in "}])":
                if not stack or brackets[stack.pop()] != b:
                    return False
            else:
                stack.append(b)
        return len(stack) == 0