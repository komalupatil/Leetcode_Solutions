#Leetcode 387. First Unique Character in a String

class Solution1:
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

class Solution2:
    def firstUniqChar(self, s: str) -> int:
        letters='abcdefghijklmnopqrstuvwxyz'
        index = []
        for l in letters:
            if s.count(l) == 1:
                index.append(s.index(l))
        return min(index) if len(index) > 0 else -1