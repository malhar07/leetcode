class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack = []

        # for i in asteroids:
        #     if not stack or not(i <0 and stack[-1]>0):
        #         stack.append(i)
        #     else:
        #         while stack and (i<0 and stack[-1]>0):
        #             curr = stack.pop()
        #             if abs(i) > curr:
        #                 curr = i
        #             else:
        #                 break
        #         if abs(i)!=curr:
        #                 stack.append(curr)
        # return stack

        stack = []
        for i in asteroids:
            if i < 0:
                if not stack or stack[-1] < 0:
                    stack.append(i)
                else:
                    while stack and stack[-1]>0 and abs(i) > abs(stack[-1]):
                        stack.pop()
                    if not stack or stack[-1]<0:
                        stack.append(i)
                    elif stack and stack[-1] == abs(i):
                        stack.pop()
            else:
                stack.append(i)
        return stack
                    