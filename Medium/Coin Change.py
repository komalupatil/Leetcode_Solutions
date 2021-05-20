#Leetcode 322. Coin Change

#TLE
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = self.helper(coins, amount)
        
        if result == float('inf'):
            return -1
        else:
            return result
        
    def helper(self, coins, amount):
        if amount == 0:
            return 0
        
        if amount < 0:
            return 0
        
        result = float('inf')
        
        for i in range(len(coins)):
            if coins[i] <= amount:
                intermediateResult = self.helper(coins, amount-coins[i])
                if intermediateResult != float('inf'):
                    result = min(result, intermediateResult+1)
        return result

#Bottom Up Approach DP
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [-1]*(amount+1)
        
        result = self.helper(coins, amount, dp)
        
        if result == float('inf'):
            return -1
        else:
            return result
        
    def helper(self, coins, amount, dp):
        if amount == 0:
            return 0
        
        if amount < 0:
            return 0
        
        if dp[amount] != -1:
            return dp[amount]
        
        result = float('inf')
        
        for i in range(len(coins)):
            if coins[i] <= amount:
                intermediateResult = self.helper(coins, amount-coins[i], dp)
                if intermediateResult != float('inf'):
                    result = min(result, intermediateResult+1)
        dp[amount] = result
        
        return dp[amount]