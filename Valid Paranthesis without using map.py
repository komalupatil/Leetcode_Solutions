#leetcode 20
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
