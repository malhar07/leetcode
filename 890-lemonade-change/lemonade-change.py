class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0,0,0,0]
        countOf5 = 0
        for bill in bills:
            change[(bill-1)//5] += 1
            diff = bill-5

            if bill == 20 and change[1] > 0:
                diff-=10
                change[1] -= 1
            
            if change[0] >= diff//5:
                change[0] -= diff//5
            else:
                return False
        return True