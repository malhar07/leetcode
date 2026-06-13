class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for char in operations:
            print(stack)
            if char == "+":
                stack.append(stack[-1]+stack[-2])
            elif char == "C":
                stack.pop()
            elif char == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(char))
            
        return sum(stack)