class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # l = 0
        # r = len(tokens)-1
        # tokens.sort()
        # score = 0
        # while l<r:
        #     if power>=tokens[l]:
        #         power-=tokens[l]
        #         l+=1
        #         score+=1
        #     else:
        #         if score>0:
        #             power+=tokens[r]
        #             r-=1
        #             score-=1
        #         else:
        #             break
        # if l==r and power>=tokens[l]:
        #     score+=1
        # return score







        score = 0
        max_score = 0
        tokens.sort()

        if not tokens or tokens[0] > power:
            return 0
        else:
            power -= tokens[0]
            score = 1
            max_score = 1
        left = 1
        right = len(tokens)-1
        while left <= right:
            
            if tokens[left] <= power:
                power-=tokens[left]
                score+=1
                left += 1
            else:
                power += tokens[right]
                score -= 1
                right -= 1
            max_score = max(score, max_score)
        return max_score

        