class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        count = 0
        for i in range(len(position)):
            stack.append((position[i], speed[i]))
        stack = sorted(stack)
        # print(stack)

        while stack:

            curr = (target - stack[-1][0]) / stack[-1][1]
            stack.pop()
            while stack and(target - stack[-1][0])/ stack[-1][1] <= curr:
                stack.pop()
            # print(stack)
            count+=1
            # print(count)
        return count