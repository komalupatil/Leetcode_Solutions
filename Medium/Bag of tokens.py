#Leetcode 948. Bag of Tokens

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        i = 0
        j = len(tokens) - 1
        maxPoints = 0
        points = 0
    
        while i <= j:
            if P >= tokens[i]:
                points +=1
                P = P - tokens[i]
                i += 1
                maxPoints = max(maxPoints, points)
            elif points > 0:
                points -= 1
                P = P + tokens[j]
                j -= 1
            else:
                return maxPoints
        return maxPoints