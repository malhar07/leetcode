class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = []
        for i in range(len(servers)):
            servers[i] = [servers[i], i]
        heapq.heapify(servers)

        busy_servers = []
        curr_time = 0
        ind = 0

            
        for i in range(len(tasks)):
            curr_time = max(curr_time,i)
            if not servers:
                curr_time = busy_servers[0][0]

            while busy_servers and busy_servers[0][0] <= curr_time:
                temp = heapq.heappop(busy_servers)
                heapq.heappush(servers, [temp[1], temp[2]])
            weight, indx = heapq.heappop(servers)
            # curr = [i+tasks[i]] + 
            res.append(indx)
            heapq.heappush(busy_servers, [curr_time+tasks[i], weight, indx])

            # curr_time += 1
        return res