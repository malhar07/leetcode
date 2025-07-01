class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = {crs:[] for crs in range(numCourses)}

        for crs, pre in prerequisites:
            adjlist[crs].append(pre)
        res = []

        def dfs(crs):
            if state[crs] == 1:
                return False
            if state[crs] == 2:
                return True
            state[crs] = 1
            for pre in adjlist[crs]:
                if not dfs(pre):
                    return False
            state[crs]=2
            res.append(crs)
            return True


        state = [0]*numCourses # 0=unvisited 1=visiting 2=visited
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res