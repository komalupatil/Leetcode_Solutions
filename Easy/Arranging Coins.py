#Leetcode 441. Arranging Coins


#Solution1

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
    


#Solution2
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        i = 1
        while n >= 0:
            n = n-i
            i += 1
        return i-2