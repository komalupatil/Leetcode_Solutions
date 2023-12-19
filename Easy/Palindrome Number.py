#Leetcode 9. Palindrome Number

#Determine whether an integer is a palindrome. 
#An integer is a palindrome when it reads the same backward as forward.

class Solution1:
    def isPalindrome(self, x: int) -> bool:
        stack = []
        for num in str(x):
            stack.append(num)

        result = ""
        for i in stack[::-1]:
            result += i
        
        return result == str(x)


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        num, result = x, 0
        while num:
            result = result*10 + num%10
            num //= 10
            
        return result == x