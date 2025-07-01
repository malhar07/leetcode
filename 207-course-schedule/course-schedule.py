class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {crs:[] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        path = set()
        memo = {}
        
        def dfs(crs):
            if crs in path:
                return False
            if crs in memo:
                return True
            path.add(crs)

            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            memo[crs] = True
            path.remove(crs)
            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        # 0: 1,2,3
        # 1:2,3
        # 2:3
        # 3:0