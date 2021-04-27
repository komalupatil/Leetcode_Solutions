#Leetcode 1816. Truncate Sentence

class Solution1:
    def truncateSentence(self, s: str, k: int) -> str:
        s= s.split()[:k]
        return " ".join(s)

class Solution2:
    def truncateSentence(self, s: str, k: int) -> str:
        for i,c in enumerate(s):
            if c == " ":
                k-= 1
                if k == 0:
                    return s[:i]
        return s