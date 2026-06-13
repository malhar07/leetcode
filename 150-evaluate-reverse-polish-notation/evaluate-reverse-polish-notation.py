class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def calculate(op1, op2, operator):
            print(op1, " ", op2)
            if operator == "+":
                return op1+op2
            elif operator == "*":
                return op1*op2
            elif operator == "-":
                return op1-op2
            else:
                return int(op1/op2)

        for char in tokens:
            if char in "+-*/":
                op2 = stack.pop()
                op1 = stack.pop()

                stack.append(calculate(op1,op2,char))
            else:
                stack.append(int(char))
            # print(stack)
        return stack[0]