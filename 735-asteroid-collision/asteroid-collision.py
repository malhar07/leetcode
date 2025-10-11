class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a < 0:
                is_valid = True
                while stack and is_valid and stack[-1] > 0:
                    if abs(stack[-1]) > abs(a):
                        is_valid = False
                        break
                    elif abs(stack[-1]) < abs(a):
                        stack.pop()
                    else:
                        stack.pop()
                        is_valid = False
                        break
                if is_valid:
                    stack.append(a)
            else:
                stack.append(a)
        return stack