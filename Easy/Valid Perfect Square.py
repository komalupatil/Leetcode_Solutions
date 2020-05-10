#Leetcode 367. Valid Perfect Square

#Solution1 - using Newton's method

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x=num
        while x*x>num:
            x = (x+num/x)//2
        return x*x==num
        

#Solution2
#Math Trick for Square number is 1+3+5+ ... +(2n-1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x,i=0,1
        while x<num:
            x +=i
            i+=2
        return x==num