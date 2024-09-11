class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dict1 = {}
        pos = [0,0]
        dict1[(pos[0], pos[1])] = 1
        

        for i in path:

            if i == "N":
                pos[1] += 1
            if i == "S":
                pos[1] -= 1
            if i == "E":
                pos[0] += 1
            if i == "W":
                pos[0] -= 1
            if (pos[0], pos[1]) in dict1:
                return True
            else:
                dict1[(pos[0], pos[1])] = 1
        return False