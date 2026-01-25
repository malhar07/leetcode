class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = -1
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                # print(stack)
                op2 = stack.pop()
                op1 = stack.pop()

                if t == "+":
                    res = op1+op2
                elif t == "-":
                    res = op1-op2
                elif t == "*":
                    res = op1*op2
                else:
                    res = int(op1/op2)
                # print(res)
                stack.append(res)
        return stack[-1]
