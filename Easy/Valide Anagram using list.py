#leetcode 3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l = []
        for ch in s:
            l.append(ch)
        for ch in t:
            if ch in l:
                l.remove(ch)
            else:
                return False
        if len(l) == 0:
            return True
