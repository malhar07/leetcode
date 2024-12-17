class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i] = tasks[i] + [i]
        print(tasks)
        tasks = sorted(tasks, key = lambda x: x[0])
        avail = []
        current_time = tasks[0][0]
        ind = 0
        res = []

        while ind < len(tasks) or len(avail)>0:
            while ind < len(tasks) and tasks[ind][0] <= current_time:
                heapq.heappush(avail, [tasks[ind][1], tasks[ind][2]])
                ind+=1
            if len(avail)>0:
                curr = heapq.heappop(avail)
                res.append(curr[1])
                current_time += curr[0]
            else:
                current_time = tasks[ind][0]
        return res