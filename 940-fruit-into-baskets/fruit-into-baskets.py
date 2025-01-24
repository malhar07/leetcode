class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # [1,2,1,2,3,4,2,2,1,3]
        dict1 = {}
        count = 0
        left = 0
        res = 0

        for i in range(len(fruits)):
            if fruits[i] in dict1:
                dict1[fruits[i]] += 1
            else:
                dict1[fruits[i]] = 1
                count+=1
                if count > 2:
                    curr = fruits[left]
                    print(curr)
                    while count > 2:
                        dict1[fruits[left]] -= 1
                        if dict1[fruits[left]] == 0:
                            del dict1[fruits[left]]
                            count-=1
                        left += 1
            res = max(res, i-left+1)
        return res

