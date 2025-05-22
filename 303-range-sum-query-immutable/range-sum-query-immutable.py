class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        self.left_map = [0]
        for i in range(len(self.nums)):
            self.left_map.append(self.left_map[i] + self.nums[i])
        print(self.left_map)

    def sumRange(self, left: int, right: int) -> int:
        # if left == 0:
        #     return self.left_map[right]
        # else:
        return self.left_map[right+1] - self.left_map[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)