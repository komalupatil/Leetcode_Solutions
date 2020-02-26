#leetcode125: Valid Palindrome

#Solution 1 : Using isalnum() func

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(i.lower() for i in s if i.isalnum())
        return s == s[::-1]

    
