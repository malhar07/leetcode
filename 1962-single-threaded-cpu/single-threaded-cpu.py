class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        arr = []
        for ind, t in enumerate(tasks):
            arr.append([t[0], t[1], ind])
        tasks = arr
        heapq.heapify(tasks)
        res = []
        process = [] #[processing_time, ind]

        # curr_time = tasks[0][0]
        curr_time = 1
        while tasks or process:
            # curr_time += 
            if not process and curr_time < tasks[0][0]:
                curr_time = tasks[0][0]

            while tasks and tasks[0][0] <= curr_time:
                enq_t, proc_t, ind = heapq.heappop(tasks)
                heapq.heappush(process, [proc_t, ind])
            proc_t, ind = heapq.heappop(process)
            res.append(ind)
            curr_time += proc_t
        return res