class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict1 = defaultdict(int)
        maxf = 0
        count = 0
        for i in tasks:
            if dict1[i] == 0:
                count +=1
            dict1[i] +=1
            maxf = max(maxf, dict1[i])
        
        x = maxf-1
        x = x*n
        flag = 1
        for key, value in dict1.items():
            if value == maxf and flag == 1:
                flag = 0
                continue
            x = x - min(maxf-1, value)
            
        # x-=count-1
        print(dict1, " ", x)
        return len(tasks) + x if x > 0 else len(tasks)