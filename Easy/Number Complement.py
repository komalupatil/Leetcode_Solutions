#Leetcode 476. Number Complement

#Solution

class Solution:
    def findComplement(self, num: int) -> int:
        temp = num
        bit = 1
        while temp != 0:
            #xor of num with 1, each digit at a time
            num = num ^ bit
            #need to shift bit to take xor each time with other digit
            bit = bit << 1
            #to know when to stop shifting bit to the left, we also need to shift num (temp)
            temp = temp >> 1
        return num