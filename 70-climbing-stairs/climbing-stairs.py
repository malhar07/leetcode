class Solution:
    def climbStairs(self, n: int) -> int:
        # if n < 3:
        #     return n
        arr = [0]*(n+2)

        arr[1] = 1
        arr[2] = 2
        step = 3

        while step<=n:
            arr[step] = arr[step-1] + arr[step-2]
            step+=1
        return arr[n]