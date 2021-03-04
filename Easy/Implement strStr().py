#Leetcode 28. Implement strStr()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if len(needle) == 0 or needle == None: 
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+n] == needle:
                    return i
        return -1