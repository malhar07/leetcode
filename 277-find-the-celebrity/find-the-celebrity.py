# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        index = 1
        while index < n:
            if knows(candidate, index):
                candidate = index
            index += 1
        
        def check_candidate(candidate):
            for i in range(n):
                if i != candidate and (not knows(i,candidate) or knows(candidate,i)):
                    return -1
            return candidate
        return check_candidate(candidate)
        
