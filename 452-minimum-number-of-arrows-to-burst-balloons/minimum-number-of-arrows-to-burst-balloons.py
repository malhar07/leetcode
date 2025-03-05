class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = []
        count=1
        points.sort()
        res.append(points[0])
        for i in range(1,len(points)):
            if points[i][0] <= res[-1][1]:
                res[-1][0] = min(res[-1][0], points[i][0])
                res[-1][1] = min(res[-1][1], points[i][1])
            else:
                res.append(points[i])
                count+=1
        return count