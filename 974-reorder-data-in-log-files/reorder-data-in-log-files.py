# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         res = []
#         digit = []
#         for log in logs:
#             l = log.split(" ")
#             if not l[-1].isdigit():
#                 res.append([log, log[len(l[0])+1:]])
#             else:
#                 digit.append(log)
#         res = sorted(res, key = lambda x: x[1])

#         for i in range(len(res)):
#             res[i] = res[i][0]
#         res += digit
#         return res

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)