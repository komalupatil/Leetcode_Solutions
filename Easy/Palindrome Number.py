#Leetcode 9. Palindrome Number

#Determine whether an integer is a palindrome. 
#An integer is a palindrome when it reads the same backward as forward.

#Solution

class Solution:
    def isPalindrome(self, x: int) -> bool:
        stack = []
        
        for num in str(x):
            stack.append(num)
        
        
        print(stack)
        
        result = ""
        
        for i in stack[::-1]:
            result += i
        
        print(result)
        
        return result == str(x)

#Solution 2

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        p, res = x, 0
        
        while p:
            res = res*10 + p %10
            print(res)
            p //= 10
            
        return res == x