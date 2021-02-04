#Leetcode 20. Valid Parentheses

#Solution1 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "[":
                stack.append("]")
            elif i == "{":
                stack.append("}")
            elif i == "(":
                stack.append(")")
            else:
                if not stack or i != stack.pop(): #condition to check if only closing is present and valid pairs
                    return False
        if stack:         #condition to check if only opening paranthesis present
            return False
        else:
            return True

#Solution2
class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '[':']', '{':'}'}
        stack = []
        open_para = set('([{')

        for bracket in s:
            if bracket in open_para:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                last_open = stack.pop()
                if d[last_open] is not bracket:
                    return False
        return len(stack) ==  0


