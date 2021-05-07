#leetcode 461. Hamming Distance

class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y
        y = 0
        while x:
            y += 1 # add (x & 1) here for (x >>1)
            x = x & (x-1) #same as (x >> 1) right shift x by 1
        return y

class Solution2:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')

class Solution3:
    def hammingDistance(self, x, y):
        ans = 0
        while x or y:
          ans += (x % 2) ^ (y % 2)
          x /= 2
          y /= 2
        return ans