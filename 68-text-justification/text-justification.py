class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        arr, res = [], []
        count = 0
        ind = 0
        
        while ind<len(words):
            arr.append([words[ind]])
            curr_length = len(words[ind])
            ind+=1
            gaps = 0
            while ind< len(words) and curr_length < maxWidth:
                # print(words[ind], " ",curr_length)
                if curr_length + len(words[ind]) + 1 <= maxWidth:
                    curr_length += len(words[ind]) + 1
                    arr[-1].append(words[ind])
                    ind+=1
                    gaps+=1
                else:
                    
                    break
            arr[-1].append(maxWidth-curr_length)
            arr[-1].append(gaps)
        print(arr)

        for i in range(len(arr)-1):
            s = ""
            gaps = arr[i].pop()
            rem = arr[i].pop()

            if gaps == 0:
                s+=arr[i][0] + " "*(rem)
                res.append(s)
            else:
                s+=arr[i][0]
                print(rem, " ", gaps)
                extra = rem%gaps
                rem = rem//gaps
                for j in range(gaps):
                    s += " "*(rem+1)
                    if extra>0:
                        s+=" "
                        extra-=1
                    s+=arr[i][j+1]
                res.append(s)
        s = arr[-1][0]
        for i in range(1,len(arr[-1])-2):
            s+=" "+arr[-1][i]
        s+= " "*(maxWidth - len(s))
        res.append(s)

        # print(res)
        return res

            
