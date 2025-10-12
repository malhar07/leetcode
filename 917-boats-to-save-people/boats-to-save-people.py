class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        right = len(people)-1
        left = 0
        num_of_boats = 0
        while left <= right:
            if people[right]+people[left] <= limit:
                left += 1
            num_of_boats+=1
            right -=1
        return num_of_boats
