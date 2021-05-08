# Leetcode 125. Valid Palindrome

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(i.lower() for i in s if i.isalnum())
        return s == s[::-1]

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        
        while l<r:
            while l<r and not s[l].isalnum():
                l += 1
            while l< r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    
