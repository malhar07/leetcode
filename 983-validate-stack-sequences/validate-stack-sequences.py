class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        ind=0

        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[ind]:
                stack.pop()
                ind+=1
            
            
        print(stack)
        return len(stack) == 0