#Leetcode 7. Reverse Integer

class Solution1:
    def reverse(self, x):
        if x < 0:
            return -1 * self.reverse(-x)
        rev = 0
        while x != 0:
            remainder = x % 10
            rev = rev * 10 + remainder
            x = x // 10
        if rev > 2147483647:
            return 0
        else:
            return rev

class Solution2:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -1 * self.reverse(-x)
        result = 0
        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x = int(x / 10)
			
        return 0 if result > pow(2, 31) - 1 or result < -pow(2, 31) else result