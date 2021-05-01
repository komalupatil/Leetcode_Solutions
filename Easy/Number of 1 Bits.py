#Leetcode 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        mask = 1
        for i in range(32):
            if (n&mask)!= 0:
                ans += 1
            mask <<= 1
        return ans