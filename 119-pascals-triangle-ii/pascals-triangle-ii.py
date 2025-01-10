class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = [1,1]
        for i in range(2,rowIndex+1):
            for j in range(len(res)-1, 0, -1):
                res[j] = res[j] + res[j-1]
            res.append(1)
        return res
            


