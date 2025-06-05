class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        arr = [1,2]
        step = 3

        while step<=n:
            
            temp = arr[1]
            arr[1] += arr[0]
            arr[0] = temp

            step+=1
        return arr[1]