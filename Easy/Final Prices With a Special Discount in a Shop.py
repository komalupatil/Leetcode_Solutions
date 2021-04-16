#Leetcode 1475. Final Prices With a Special Discount in a Shop

#Solution - Monotonic stack
## build a increasing stack while finding next smaller element

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        if len(prices) == 0:
            return []
        stack = []
        result = prices
        
        for i in range(len(prices)):
            while stack and result[stack[-1]] >= prices[i]:
                index = stack.pop()
                result[index] = prices[index] - prices[i]
            stack.append(i)
        return result