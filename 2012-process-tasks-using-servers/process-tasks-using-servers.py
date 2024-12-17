class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        busy = []
        res = []
        for i in range(len(servers)):
            servers[i] = (servers[i], i)
        heapq.heapify(servers)
        q = deque()
        indx = 0

        time = 0

        while indx<len(tasks) or busy:
            # if time<len(tasks):
            #     q.append(tasks[time])
            while len(busy)>0 and busy[0][0] <= time:
                end_time, serv, ind = heapq.heappop(busy)
                heapq.heappush(servers, (serv, ind))
            while len(servers) > 0 and indx<len(tasks) and indx<=time:
                serv, ind = heapq.heappop(servers)
                res.append(ind)
                end_time = time + tasks[indx]
                indx+=1
                heapq.heappush(busy, (end_time, serv, ind))
            if not servers and busy:
                time = busy[0][0]   
            else:         
                time+=1
        return res

