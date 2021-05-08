#Leetcode 367. Valid Perfect Square

#using Newton's method
class Solution1:
    def isPerfectSquare(self, num: int) -> bool:
        x=num
        while x*x>num:
            x = (x+num/x)//2
        return x*x==num
        
#Math Trick for Square number is 1+3+5+ ... +(2n-1)
class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        x,i=0,1
        while x<num:
            x +=i
            i+=2
        return x==num

# binary search approach
class Solution3:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        
        while l<=r:
            mid = l+ (r-l)//2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                r = mid -1
            else:
                l = mid+1
        return False