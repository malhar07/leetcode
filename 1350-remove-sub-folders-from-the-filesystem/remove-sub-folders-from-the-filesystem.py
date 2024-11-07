class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        dict1 = {}
        for f in folder:
            dict1[f] = f.split("/")[1:]
        print(dict1)
        
        for f in folder:
            s = ""
            if len(dict1[f]) == 1:
                continue
            for i in dict1[f][:-1]:
                s+="/" + i
                if s in dict1:
                    del dict1[f]
                    break
            
        return list(dict1.keys())
