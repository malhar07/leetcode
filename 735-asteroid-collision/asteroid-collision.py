class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if stack and stack[-1] > 0 and a < 0:
                while stack and stack[-1] > 0:
                    if abs(a) > abs(stack[-1]):
                        stack.pop()
                    elif abs(a) == abs(stack[-1]):
                        stack.pop()
                        a = 0
                        break
                    else:
                        break
                
                if (not stack or stack[-1] < 0) and a!=0:
                    stack.append(a)
            else:
                stack.append(a)
        return stack