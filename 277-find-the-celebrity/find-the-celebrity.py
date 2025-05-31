# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        index = 1
        cache = {}
        while index < n:
            if knows(candidate, index):
                cache[(candidate, index)] = True
                candidate = index
            else:
                cache[(candidate,index)] = False
            index += 1
        
        def check_candidate(candidate):
            for i in range(n):
                if i == candidate:
                    continue
                if not knows(i,candidate) or knows(candidate,i):
                    return -1
            return candidate
        return check_candidate(candidate)
        
