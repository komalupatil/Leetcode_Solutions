#Leetcode 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        max_len = 1
        n = len(s)

        res = ""
        for i in range(n-1):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            
            tmp = self.helper(s, i, i+1)
            if len(tmp)> len(res):
                res = tmp
        return res
    
    def helper(self,s, l, r):
        while l>= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break

        return s[l+1:r]