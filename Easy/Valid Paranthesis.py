# Leetcode 20. Valid Parentheses

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution1:
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

class Solution2:
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


class Solution3:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        closing_brackets = []

        for bracket in s:
            if bracket == "(":
                closing_brackets.append(")")
            elif bracket == "{":
                closing_brackets.append("}")
            elif bracket == "[":
                closing_brackets.append("]")
            else:
                if not closing_brackets or closing_brackets.pop() != bracket:
                    return False
        if closing_brackets:
            return False
        return True


