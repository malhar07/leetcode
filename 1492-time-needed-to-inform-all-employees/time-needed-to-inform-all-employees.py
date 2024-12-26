class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dict1 = defaultdict(list)
        for ind, i in enumerate(manager):
            dict1[i].append(ind)
        max_time = 0
        q = deque()
        q.append((headID,0))

        while q:
            curr, time = q.popleft()
            max_time = max(max_time, time)

            for employee in dict1[curr]:
                q.append((employee, time+informTime[curr]))
            
        return max_time
            # for i in range(len(q)):
        #         curr = q.popleft()
        #         level_time = max(level_time, informTime[curr])
        #         if curr in dict1:
        #             for employee in dict1[curr]:
        #                 q.append(employee)
                
        #     time+=level_time
        # return time
