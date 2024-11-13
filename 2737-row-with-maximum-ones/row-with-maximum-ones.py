class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [0,0]
        count = 0
        for m in range(len(mat)):
            count = 0
            for n in mat[m]:
                if n == 1:
                    count+=1
            if count > res[1]:
                res[0] = m
                res[1] = count
        return res