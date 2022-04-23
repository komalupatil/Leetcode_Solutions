#Leetcode 2144. Minimum Cost of Buying Candies With Discount

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]
        
        result = 0
        cost.sort()
           
        i = len(cost) - 1  
        while i >= 0:
            result += cost[i]
            i -= 1
            if i >= 0:
                result += cost[i]
                i -= 1
            i -= 1
            
        return result