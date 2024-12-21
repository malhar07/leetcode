class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # res =[]
        # products = sorted(products)

        # for ind, i in enumerate(searchWord):
        #     arr = []
        #     for j in products:
        #         if len(arr) == 3:
        #             break
        #         if len(j) < ind+1:
        #             continue
        #         if searchWord[:ind+1] == j[:ind+1]:
        #             arr.append(j)
        #     res.append(arr)
        # return res
        res =[]
        products = sorted(products)

        for ind, i in enumerate(searchWord):
            arr = []
            left = 0
            right = len(products)-1
            curr = -1
            while left <= right:
                mid = (left+right)//2

                if searchWord[:ind+1] < products[mid][:ind+1]:
                    right = mid-1
                elif searchWord[:ind+1] > products[mid][:ind+1]:
                    left = mid+1
                else:
                    curr = mid
                    right = mid-1
            if curr == -1:
                res.append([])
            else:
                for j in range(curr, min(curr+3, len(products))):
                    if products[j][:ind+1] == searchWord[:ind+1]:
                        arr.append(products[j])
                    else:
                        break
                res.append(arr)
        return res
                
                

