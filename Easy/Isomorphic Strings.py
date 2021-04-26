#Leetcode 205. Isomorphic Strings

#Similar problem : Leetcode 290. Word Pattern
#Solution
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        
        d  = {}
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] in d:
                if d[s[i]] != t[j]:
                    return False
            else:
                if t[j] in d.values():
                    return False
                d[s[i]]  = t[j]
            i += 1
            j += 1
        return True
