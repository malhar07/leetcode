class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        n = num.copy()
        

        n.sort(reverse = True)
        
        for i in range(len(n)):
            if int(n[i]) != int(num[i]):
                break
        small = num[i]
        big = n[i]
        print(big, " ", small)
        num[i] = n[i]
        # print(n)
        print(num)
        for i in range(len(num)-1, -1, -1):
            if num[i] == big:
                num[i] = small
                break
        return int("".join(num))
        