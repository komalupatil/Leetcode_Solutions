#Leetcode 202. Happy Number

#Write an algorithm to determine if a number is "happy".

#A happy number is a number defined by the following process: Starting with any positive integer, replace the number by 
# the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

#Example: 

#Input: 19
#Output: true
#Explanation: 
#1^2 + 9^2 = 82
#8^2 + 2^2 = 68
#6^2 + 8^2 = 100
#1^2 + 0^2 + 0^2 = 1

#once the number is repeated return false
class Solution1:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = sum(int(i)**2 for i in str(n))
            if n==1:
                return True
        return False

#Slow and fast pointer approach
class Solution2:
    def isHappy(self, n: int) -> bool:
        slow,fast = n,n
        while True:
            slow = self.find_square_sum(slow)
            fast = self.find_square_sum(self.find_square_sum(fast))
            if slow == fast:
                break
        return slow == 1
    
    def find_square_sum(self, num):
        _sum = 0
        while num>0:
            digit = num%10
            _sum += digit*digit
            num//=10
        return _sum