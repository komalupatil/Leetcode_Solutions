#Leetcode 14. Longest Common Prefix

#Solution

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        minLength = len(strs[0])
        
        for i in range(1, len(strs)):
            minLength = min(len(strs[i]), minLength)
            
        i = 0
        lcp = ""
        
        while i < minLength:
            char = strs[0][i]
            for j in range(1, len(strs)):
                if char != strs[j][i]:
                    return lcp
            lcp = lcp + char
            i = i + 1
        return lcp