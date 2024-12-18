class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(op1, op2, operator):
            if operator == "+":
                return op1+op2
            if operator == "-":
                return op1-op2
            if operator == "*":
                return op1*op2
            if operator == "/":
                return int(op1/op2)
        
        stack = []

        for char in tokens:
            # if stack:
            #     print(stack[-1])
            if char not in ["+", "-", "*", "/"]:
                stack.append(int(char))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                print(op1, " ", op2, " ", char)
                stack.append(operation(op1, op2, char))
        return stack[0]