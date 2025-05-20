class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 1
        total = 0
        while left < len(height) and height[left] == 0:
            print(left)
            left+=1
        right = left+1

        #first pass
        while right < len(height):
            if height[right] >= height[left]:
                current_height = height[left]

                while left<right:
                    total+= current_height - height[left]
                    left+=1
                
            right+=1
        #second pass
        right-=1
        left_boundary = left
        left = right-1
        print(left, " ", right, " ", left_boundary)
        while left >= left_boundary:
            if height[left] >= height[right]:
                current_height = height[right]

                while right > left:
                    total += current_height - height[right]
                    right -= 1
            left-= 1
        return total