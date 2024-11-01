class Solution:
    def reorganizeString(self, s: str) -> str:
        dict1 = defaultdict(int)
        for i in s:
            dict1[i] += 1
        
        sorted_dict = sorted(dict1.items(), key = lambda x: x[1], reverse = True)

        res = ['']*len(s)
        ind = 0
        if sorted_dict[0][1] > (len(s)+1)//2:
                return ""
        for char, count in sorted_dict:
            
            for i in range(count):
                print(ind)
                if ind >= len(s):
                    ind = 1
                res[ind] = char
                ind+=2
                
        
        return "".join(res)
        print(sorted_dict)