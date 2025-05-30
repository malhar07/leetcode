class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        not_judge = set()
        trust_dict = defaultdict(int)
        result = -1
        for p1, p2  in trust:
            not_judge.add(p1)
            trust_dict[p2] += 1
        for i in range(1,n+1):
            if i not in not_judge:
                if trust_dict[i] == n-1:
                    return i
                return -1
                # if result== -1:
                #     result =  i
                # else:
                #     return -1

        return result