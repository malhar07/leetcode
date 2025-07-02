class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_set = set(folder)
        res = []
        for f in folder:
            path = f.split('/')[1:-1]
            sub_folder = ""
            parent_folder_present = False
            for file in path:
                sub_folder += "/" + file
                if sub_folder in folder_set:
                    parent_folder_present = True
                    break
            if not parent_folder_present:
                res.append(f)
        return list(res)