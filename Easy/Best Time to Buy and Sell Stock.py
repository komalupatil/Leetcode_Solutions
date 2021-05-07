#Leetcode 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1:
            return 0
        minimum = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i]- minimum > max_profit:
                max_profit = prices[i] - minimum
        return max_profit
