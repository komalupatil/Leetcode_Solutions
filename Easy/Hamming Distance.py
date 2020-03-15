#leetcode 461. Hamming Distance


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y
        y = 0
        while x:
            y += 1 # add (x & 1) here for (x >>1)
            x = x & (x-1) #same as (x >> 1) right shift x by 1
        return y
