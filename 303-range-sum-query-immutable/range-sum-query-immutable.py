class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dict1 = {}
        self.total = sum(self.nums)
        self.left_map = [0]*len(self.nums)
        self.right_map = [0]*len(self.nums)
        for i in range(1,len(self.nums)):
            self.left_map[i] = self.left_map[i-1] + self.nums[i-1]
        for i in range(len(self.nums)-2, -1, -1):
            self.right_map[i] = self.right_map[i+1] + self.nums[i+1]
        print(self.left_map)
        print(self.right_map)




    def sumRange(self, left: int, right: int) -> int:
        return self.total - self.left_map[left] - self.right_map[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)