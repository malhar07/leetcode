class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res =[]
        products = sorted(products)

        for ind, i in enumerate(searchWord):
            arr = []
            for j in products:
                if len(arr) == 3:
                    break
                if len(j) < ind+1:
                    continue
                if searchWord[:ind+1] == j[:ind+1]:
                    arr.append(j)
            res.append(arr)
        return res
                

