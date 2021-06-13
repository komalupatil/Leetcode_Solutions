#Leetcode 1614. Maximum Nesting Depth of the Parentheses

class Solution1:
    def maxDepth(self, s: str) -> int:
        pair = []
        maxDepth = 0
    
        for i in s:
            if i == "(":
                pair.append(')')
                maxDepth = max(maxDepth, len(pair))
            if i == ")":
                if pair:
                    pair.pop()
                maxDepth = max(maxDepth, len(pair))
        return maxDepth

class Solution2:
    def maxDepth(self, s: str) -> int:
        pair = 0
        maxDepth = 0
    
        for i in s:
            if i == "(":
                pair += 1
                maxDepth = max(maxDepth, pair)
            if i == ")":
                pair -= 1
                maxDepth = max(maxDepth, pair)
        return maxDepth