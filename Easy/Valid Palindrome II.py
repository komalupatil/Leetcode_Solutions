#Leetcode 680. Valid Palindrome II

class Solution1:
    def validPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) -1
        
        while p1<p2:
            if s[p1] != s[p2]:
                one, two = s[p1:p2], s[p1+1:p2+1]
                return one == one[::-1] or two == two[::-1]
            p1+=1
            p2-=1
        return True

class Solution2:
    def validPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) -1
        
        while p1<p2:
            if s[p1] != s[p2]:
                if (self.isPalindrome(s, p1+1, p2) or self.isPalindrome(s, p1, p2-1)):
                    return True
                else:
                    return False
            p1+= 1
            p2-= 1
        return True
    
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True