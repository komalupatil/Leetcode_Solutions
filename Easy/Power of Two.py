#Leetcode 231. Power of Two

#Bit manipulation. Power of 2 means only one bit of n is '1', hence using n&(n-1) == 0.  
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<= 0:
            return False
        else:
            return not (n&(n-1))