class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = sum(students)
        zeroes = len(students) - ones

        for i in sandwiches:
            if i == 1:
                if ones == 0:
                    break
                ones -= 1
            else:
                if zeroes == 0:
                    break
                zeroes -= 1
        return zeroes + ones
            