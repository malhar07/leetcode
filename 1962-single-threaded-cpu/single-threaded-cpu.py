class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        res = []
        curr_time = 0
        for i in range(len(tasks)):
            tasks[i] = tasks[i] + [i]
        tasks.sort(key = lambda x: x[0])

        ind = 0
        curr_time = tasks[0][0]
        while heap or ind < len(tasks):
            print(curr_time)
            
            while ind < len(tasks) and tasks[ind][0] <= curr_time:
                heapq.heappush(heap, [tasks[ind][1], tasks[ind][2]])
                ind+=1
            if not heap:
                curr_time = tasks[ind][0]
            else:
                proc_time, index = heapq.heappop(heap)
                # print(proc_time, " ", index)
                res.append(index)
                curr_time += proc_time
            # if not heap and ind<len(tasks):
            #     curr_time = max(curr_time, tasks[ind][0])
        
        return res



