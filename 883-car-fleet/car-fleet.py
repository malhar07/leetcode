class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        res = 0

        for pos, sp in zip(position, speed):
            t = (target-pos) / sp
            time.append([pos,t])
        time.sort()

        ind = len(time)-1

        while ind >= 0:
            curr_time = time[ind][1]
            while ind>=0 and time[ind][1] <= curr_time:
                ind-=1
            res += 1
        return res