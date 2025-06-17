class SnapshotArray:

    def __init__(self, length: int):
        self.snapshot = {}
        for i in range(length):
            self.snapshot[i] = [(0,0)]
        self.length = length
        
        self.s_id = 0

    def set(self, index: int, val: int) -> None:
        self.snapshot[index].append((val,self.s_id))


    def snap(self) -> int:
        # self.snapshot[]
        self.s_id += 1
        return self.s_id-1



    def get(self, index: int, snap_id: int) -> int:
        arr = self.snapshot[index]
        left = 0
        right = len(arr)-1

        while left <= right:
            mid = left + (right-left)//2
            if arr[mid][1] <= snap_id:
                left = mid+1
            else:
                right = mid-1
        return arr[right][0]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)