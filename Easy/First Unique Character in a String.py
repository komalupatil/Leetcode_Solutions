#Leetcode 387. First Unique Character in a String

#Solution 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == "":
            return -1
        
        d = {}
        
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        for i,char in enumerate(s):
            if d[char] == 1:
                return i
        return -1