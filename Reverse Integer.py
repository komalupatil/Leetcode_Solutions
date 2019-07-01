class Solution:
    def reverse(self, x):
        if x < 0:
            return -1 * self.reverse(-x)
        rev = 0
        while x != 0:
            remainder = x % 10
            rev = rev * 10 + remainder
            x = x // 10
        if int(rev) > 2147483647:
            return 0
        else:

            return int(rev)