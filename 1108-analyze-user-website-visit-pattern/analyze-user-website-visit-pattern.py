class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        dict1 = {}
        for ind, user in enumerate(username):
            if user not in dict1:
                dict1[user] = []
            dict1[user].append((website[ind], timestamp[ind]))
        res = defaultdict(int)
        for key, val in dict1.items():
            visited = set()
            if len(val) < 3:
                continue
            val = sorted(val, key = lambda x: x[1])
            # print(val)

            for i in range(len(val)-2):
                for j in range(i+1, len(val)-1):
                    for k in range(j+1, len(val)):
                        if (val[i][0], val[j][0], val[k][0]) not in visited:
                            res[(val[i][0], val[j][0], val[k][0])]+=1
                            visited.add((val[i][0], val[j][0], val[k][0]))
                        
        # res = sorted(res, key = lambda x: x[0])

        print(res)
        ans = []
        count = 0
        for key, val in res.items():
            if val > count:
                ans = key
                count = val
            elif val == count:
                if ans < key:
                    continue
                else:
                    ans = key
                    count = val

        return list(ans)