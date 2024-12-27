class Solution:
    def numTrees(self, n: int) -> int:
        dict1 = {}
        def helper(num):
            if 0<=num<=2:
                    return num
            curr = 0
            for i in range(1, num+1):
                if (i-1) in dict1:
                    left = dict1[i-1]
                else:
                    left = max(1,helper(i-1))
                    dict1[i-1] = left
                if num-i in dict1:
                    right = dict1[num-i]
                else:
                    right = max(1,helper(num-i))
                    dict1[num-i] = right
                
                curr+= left*right
            return curr
        return helper(n)