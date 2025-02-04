class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            if not stack or not(i <0 and stack[-1]>0):
                stack.append(i)
            else:
                while stack and (i<0 and stack[-1]>0):
                    
                    curr = stack.pop()
                    if abs(i) > curr:
                        curr = i
                    else:
                        break
                    # elif abs(i) < curr:
                    #     break                 
                    # else:
                    #     break
                if abs(i)!=curr:
                        stack.append(curr)
            # print(stack)
        return stack
                    