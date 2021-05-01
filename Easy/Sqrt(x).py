#Leetcode 69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x
        
        while left < right:
            mid = left + (right-left)//2
            if mid <= x/mid and (mid+1) > x/(mid+1):
                return mid
            elif mid > x/mid:
                right = mid - 1
            else:
                left = mid + 1
        return left