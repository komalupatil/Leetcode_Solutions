#leetcode172. Factorial Trailing Zeroes
#Trailing 0s in n! = Count of 5s in prime factors of n!
#                  = floor(n/5) + floor(n/25) + floor(n/125) + ....
class Solution:
    def trailingZeroes(self, n: int) -> int:
        k, cnt = 5, 0
        while k <= n:
            cnt += n // k
            k = k * 5
        return cnt
