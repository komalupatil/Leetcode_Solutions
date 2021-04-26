#Leetcode 290. Word Pattern

#Solution - similar to Leetcode 205. Isomorphic Strings

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern or not s:
            return False  

        d = {}
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        i = 0
        j = 0
        while i < len(pattern) and j < len(s):
            if pattern[i] in d:
                if d[pattern[i]] != s[j]:
                    return False
            else:
                if s[j] in d.values():
                    return False
                d[pattern[i]] = s[j]
            i += 1
            j += 1
        return True