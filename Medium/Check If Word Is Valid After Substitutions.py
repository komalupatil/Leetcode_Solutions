#Leetcode 1003. Check If Word Is Valid After Substitutions

#Solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == 'c':
                if stack[-2:] != ['a', 'b']:
                    return False
                stack.pop()
                stack.pop()
            else:
                stack.append(i)
        return not stack