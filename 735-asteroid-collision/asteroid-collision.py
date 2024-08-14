class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1,len(asteroids)):
            if asteroids[i] < 0 and stack and stack[-1] > 0:
                current = asteroids[i]*-1
                while stack and stack[-1] > 0:
                    if current > stack[-1]:
                        stack.pop()
                    elif current == stack[-1]:
                        current=0
                        stack.pop()
                        break
                    else:
                        current = 0
                        break
                if current != 0:
                    stack.append(current*-1)
            else:
                stack.append(asteroids[i])
        return stack