class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # arr = []
        # for i in range(len(s)):
        #     arr.append(abs(ord(s[i]) - ord(t[i])))

        # cost = 0
        # left = 0
        # right = 0
        # max_len = 0
        # while right < len(s):
        #     if cost + arr[right] <= maxCost:
        #         cost += arr[right]
        #         right += 1
        #     else:
        #         cost += arr[right] - arr[left]
        #         right += 1
        #         left +=1
        #     if cost <= maxCost:
        #         max_len = max(max_len, right - left)
        # return max_len

        # arr = []
        # for i in range(len(s)):
        #     arr.append(abs(ord(s[i]) - ord(t[i])))

        cost = 0
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            x = abs(ord(s[right]) - ord(t[right]))
            y = abs(ord(s[left]) - ord(t[left]))
            if cost + x <= maxCost:
                cost += x
                right += 1
            else:
                cost += x - y
                right += 1
                left +=1
            if cost <= maxCost:
                max_len = max(max_len, right - left)
        return max_len
        
