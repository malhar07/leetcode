class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        arr = [0] * len(dominoes)
        direction = "N"
        count = -len(dominoes)
        print(count)
        #left to right
        for ind, i  in enumerate(dominoes):
            if i == "R":
                direction = "R"
                count = -len(dominoes)
            if i == "L":
                direction = "L"
            if i == ".":
                if direction == "R":
                    arr[ind] += count
                    count += 1
        print(arr)
        #right to left
        count = len(dominoes)
        ind = len(dominoes)-1
        direction = "N"
        while ind >= 0:
            if dominoes[ind] == "R":
                direction = "R"
            if dominoes[ind] == "L":
                direction = "L"
                count = len(dominoes)
            if dominoes[ind] == ".":
                if direction == "L":
                    arr[ind] += count
                    count -= 1
            ind-=1
        res = ""

        for ind, i in enumerate(dominoes):
            if i == "L":
                res+="L"
            elif i == "R":
                res+="R"
            else:
                if arr[ind]>0:
                    res+="L"
                elif arr[ind] <0:
                    res+="R"
                else:
                    res+="."
        print(arr)
        return res 