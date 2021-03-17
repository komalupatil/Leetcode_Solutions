#Leetcode 374. Guess Number Higher or Lower

#Solution - binary search

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        h = n
        while l<=h:
            mid = l+(h-l)//2
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == -1:
                h = mid - 1
            else:
                l = mid + 1