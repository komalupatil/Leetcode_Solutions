#Leetcode 1249. Minimum Remove to Make Valid Parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = set()
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    res.add(i)
        while stack:
            res.add(stack.pop())
        
        ans = ""
        for i in range(len(s)):
            if i not in res:
                ans += s[i]
        
        return ans