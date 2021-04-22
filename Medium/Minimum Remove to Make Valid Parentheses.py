#Leetcode 1249. Minimum Remove to Make Valid Parentheses

#Solution
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = set() 
        
        for i in range(len(s)):
            if s[i] == ')' and len(stack) == 0:
                res.add(i)
            elif s[i] == ')' and len(stack) != 0:
                stack.pop()
            else:
                if s[i] == '(':
                    stack.append(i)
        while stack:
            res.add(stack.pop())
        
        result = ""
        
        for i in range(len(s)):
            if i not in res:
                result += s[i]
        return result