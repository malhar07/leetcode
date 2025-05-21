class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            result = []
            len1 = len(left)
            len2 = len(right)
            ind1 = ind2 = 0
            while ind1<len1 and ind2<len2:
                if left[ind1] <= right[ind2]:
                    result.append(left[ind1])
                    ind1+=1
                else:
                    result.append(right[ind2])
                    ind2+=1
            if ind1 == len1:
                result.extend(right[ind2:])
            else:
                result.extend(left[ind1:])
            return result
                
        def merge_sort(s, e):
            if s == e:
                return [nums[s]]
            mid = s + (e-s)//2
            left = merge_sort(s, mid)
            right = merge_sort(mid+1,e)

            return merge(left, right)
        s = 0
        e = len(nums)-1
        return merge_sort(s,e)