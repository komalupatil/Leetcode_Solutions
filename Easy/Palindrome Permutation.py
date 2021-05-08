#Leetcode 266. Palindrome Permutation

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        d = {}

        for i in s:
            if i in d and d[i] > 0:
                d[i] -=1      
            else:
                d[i] = 1
        
        count = 0
        
        for v in d.values():
            if count > 1:
                return False
            
            if v == 1:
                count += 1
        
        return count < 2
        



