#Leetcode 441. Arranging Coins


#Solution

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n >= i:
            n = n-i
            i= i+1
        if i == n:
            return i
        else:
            return i-1
    