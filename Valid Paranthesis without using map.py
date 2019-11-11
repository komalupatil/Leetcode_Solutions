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
                if not stack or i != stack.pop():
                    return False
        if stack:
            return False
        else:
            return True
