#Leetcode 921. Minimum Add to Make Parentheses Valid

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        pair = 0
        invalidPair = 0
        
        for i in s:
            if i == "(":
                pair += 1
            if i == ")":
                if pair > 0:
                    pair -= 1
                else:
                    invalidPair += 1
        return pair + invalidPair