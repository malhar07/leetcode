class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a < 0:
                to_append = True
                while stack and stack[-1]>0:
                    a2 = stack.pop()
                    if a2 > abs(a):
                        stack.append(a2)
                        to_append = False
                        break
                    elif a2 == abs(a):
                        to_append = False
                        break
                if to_append:
                    stack.append(a)
            else:
                stack.append(a)
        return stack