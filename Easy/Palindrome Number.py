# Leetcode 9. Palindrome Number

"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""

"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
"""

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