#leetcode 1342. Number of Steps to Reduce a Number to Zero

class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num > 0:
            if num%2 != 0:
                num = num -1
            else:
                num = num//2
            count +=1
        return count


